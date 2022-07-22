from importlib.resources import path
import secrets
from pydub import AudioSegment
import os
import csv

data_folder = "voice1_mergeAudio_fullsubnet"
save_folder = "voice1_cutVad_fullsubnet"
refer_folder = "voice1_build"
refer_csv = "voice1_vad_fullsubnet_csv"                                                                        

#總檔數與小於4秒檔數
total_speech_file  =0

less_4sec_file  =0
#>4秒總秒數
total_less_4sec_sec = 0
#每一位語者的秒數
speakSec = None
speakSec_less4_file = None
speaker_speech_file = None
#總csv
total_csv_file =0

#至少有60s可以用的人數
total_people = 0
least_30sce_people = 0
least_60sce_people = 0
least_120sce_people = 0


csv_list = os.listdir(refer_folder)
total_csv_file = len(csv_list)

speakers = os.listdir(refer_folder)
total_people = len(speakers)

##查看csv資料回傳清單
def csv_data(csv_path):

    with open(csv_path, newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter='\t')
        rows = list(rows)
        #回傳清單
        return rows



#掃語者
for speaker in speakers:
    speakSec=0
    speaker_speech_file = 0
    speakSec_less4_file = 0
    #在儲存區創建語者資料夾
    speak_folder = os.path.join(save_folder,speaker)
    if not os.path.exists(speak_folder):
        os.mkdir(speak_folder)
    #
    speak_path = os.path.join(refer_folder,speaker)
    #掃wav
    wavs = os.listdir(speak_path)
    for wav in wavs:
        wav_folderName= wav[:-4]
        #在儲存區的語者資料夾創建wav資料夾
        speakWav_folder= os.path.join(speak_folder,wav_folderName)
        if not os.path.exists(speakWav_folder):
            os.mkdir(speakWav_folder)
        #
        #csv位置
        csv_wav_path = os.path.join(refer_csv,wav_folderName+'.csv')
        #除噪wav音檔位置
        wav_emPath = os.path.join(data_folder,speaker,wav_folderName,wav)

        data_CSV = csv_data(csv_wav_path)
        for type,start,stop in data_CSV:
            
            if type == "speech":
                #浮點數四捨五入取前兩位
                start=round(float(start),2)
                stop =round(float(stop),2)
                #總speech檔數與單位語者總speech檔數+1
                total_speech_file+=1
                speaker_speech_file+=1
                #算時間<4s去掉
                use_time=stop-start
                
                if use_time > 4:
                    #單位語者秒數累加，完畢後四捨五入取小數點前兩位
                    speakSec += use_time
                    speakSec = round(speakSec,2)
                    total_less_4sec_sec += use_time
                    total_less_4sec_sec = round(total_less_4sec_sec,2)
                    
                    #至少4秒檔數+1
                    less_4sec_file+=1
                    speakSec_less4_file+=1

                    awesome = AudioSegment.from_wav(wav_emPath)
                    #秒(sec)要表示成毫秒
                    time = awesome[start*1000:stop*1000]
                    
                    #幫名稱轉字串並補零至7個位數，方便辨識
                    start = str(start).replace('.','').zfill(7)
                    stop = str(stop).replace('.','').zfill(7)
                    wav_save_name = start + '-' + stop + '.wav'
                    wav_save_name_path = os.path.join(speakWav_folder,wav_save_name)
                    #儲存音檔
                    awesome.export(wav_save_name_path, format="wav")             
    if speakSec >= 30:
        least_30sce_people+=1
        if speakSec >= 60:
            least_60sce_people+=1
            if speakSec >= 120:
                least_120sce_people+=1
    print("第{}位語者,共{}位,該語者有{}個音檔,speech檔為{}個,可用檔案數(>4s)為{}個,可用秒數為{}秒\
    ,目前speech檔累積{}個,可用(>4秒)檔案累積{}個,可用秒數為{}秒".format(
        speakers.index(speaker)+1,
        total_people,
        len(wavs),
        speaker_speech_file,
        speakSec_less4_file,
        speakSec,
        total_speech_file,
        less_4sec_file,
        total_less_4sec_sec)
    )


with open('result_ofFullsubnet.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['總人數','{}人'.format(str(total_people))])
    writer.writerow(['scv總數','{}個'.format(str(total_csv_file))])
    writer.writerow(['speech總檔數','{}個'.format(total_speech_file)])
    writer.writerow(['speech>4秒(sec)總檔數','{}個'.format(str(less_4sec_file))])
    writer.writerow(['speech>4秒(sec)總秒數','{}秒'.format(str(total_less_4sec_sec))])
    writer.writerow(["至少30秒","{}人".format(str(least_30sce_people))])
    writer.writerow(["至少60秒","{}人".format(str(least_60sce_people))])
    writer.writerow(["至少120秒","{}人".format(str(least_120sce_people))])
    writer.writerow([])





















                




