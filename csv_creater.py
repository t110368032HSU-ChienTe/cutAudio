import os

from pydub import AudioSegment


data_folder = "voice1_cutVad_fullsubnet_180_less15"
save_folder = "results_csv"
save_file  = "sv_ecapa_10_20"

sec_min = 10
sec_max = 20

#介於兩者間清單
ecapa_10_20= {}
total_10_20= 0

total_list=[]

if not os.path.exists(save_folder):
    os.mkdir(save_folder)

speakers = os.listdir(data_folder)
#看語者們
for speaker in speakers:
    speaker_folder = os.path.join(data_folder,speaker)
    wavss = os.listdir(speaker_folder)
    #看wav資料夾
    for wavs in wavss:
        wavs_folder= os.path.join(speaker_folder,wavs)
        wavs_list = os.listdir(wavs_folder)
        #看名稱
        for wav in wavs_list:
            wav_name=os.path.join(wavs_folder,wav)
            awesome = AudioSegment.from_wav(wav_name)
            
            len_sec = len(awesome)/1000.0
            save_name = wav_name.replace(data_folder,"",1)
            if sec_min<len_sec<sec_max:
                total_10_20+=1
                
                ecapa_10_20.update({speaker:{wavs:{wav:{save_name}}}})
                print("第{}個,名稱{}".format(total_10_20,save_name))
            total_list.append([speaker,wavs,wav,save_name])


for SPK,WAVS,WAV,PATH in total_list:
    print(SPK,WAVS,WAV,PATH)









                



        
