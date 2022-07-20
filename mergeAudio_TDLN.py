import secrets
from pydub import AudioSegment
import os

data_folder = "voice1_em_DTLN"
save_folder = "voice1_mergeAudio_DTLN"
refer_folder = "voice1_cutAudio_30"


speaker_num=0
wav_num =0

speakers = os.listdir(refer_folder)

for speaker in speakers:
    #印出到第幾個人，哪一個人
    speaker_num+=1
    print("第{}個,語者:{}".format(speaker_num,speaker))

    if not os.path.exists("{}/{}".format(save_folder,speaker)):
        os.mkdir("{}/{}".format(save_folder,speaker))
    #看放wav的資料夾
    wavs_folder = os.listdir(refer_folder+'/'+speaker)

    for wav_name_folder in wavs_folder:
        #看第幾個wav檔
        wav_num+=1
        print("第{}個語音檔,檔案名{}".format(wav_num,wav_name_folder))

        #創建wav_folder
        if not os.path.exists("{}/{}/{}".format(save_folder,speaker,wav_name_folder)):
            os.mkdir("{}/{}/{}".format(save_folder,speaker,wav_name_folder))
        #看wav的名子
        wavs =  os.listdir(refer_folder+'/'+speaker+'/'+wav_name_folder)
        #先宣告第一個wav，後面再加，最後儲存
        awesome= AudioSegment.from_wav(data_folder+'/'+speaker+'/'+wav_name_folder+'/'+wavs[0])
        for wav in wavs[1:]:
            
            song = AudioSegment.from_wav(data_folder+'/'+wav_name_folder+'/'+wav)
            awesome+=song
        wav_save_name= save_folder+'/'+speaker+'/'+wav_name_folder+'/'+wav_name_folder+'.wav'
        #儲存
        awesome.export(wav_save_name, format="wav")

        


        


        
