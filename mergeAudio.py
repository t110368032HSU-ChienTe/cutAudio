import secrets
from pydub import AudioSegment
import os

save_folder = "voice1_mergeAudio"
data_folder = "voice1_cutAudio"


speakers = os.listdir(data_folder)

for speaker in speakers:
    if not os.path.exists("{}/{}".format(save_folder,speaker)):
        os.mkdir("{}/{}".format(save_folder,speaker))
    #看放wav的資料夾
    wavs_folder = os.listdir(data_folder+'/'+speaker)
    for wav_name_folder in wavs_folder:
        #創建wav_folder
        if not os.path.exists("{}/{}/{}".format(save_folder,speaker,wav_name_folder)):
            os.mkdir("{}/{}/{}".format(save_folder,speaker,wav_name_folder))
        #看wav的名子
        wavs =  os.listdir(data_folder+'/'+speaker+'/'+wav_name_folder)
        #先宣告第一個wav，後面再加，最後儲存
        awesome= AudioSegment.from_wav(data_folder+'/'+speaker+'/'+wav_name_folder+'/'+wav[0])
        for wav in wavs[1:]:
            
            song = AudioSegment.from_wav(data_folder+'/'+speaker+'/'+wav_name_folder+'/'+wav)
            awesome+=song
        wav_save_name= save_folder+'/'+speaker+'/'+wav_name_folder+'.wav'
        #儲存
        awesome.export(wav_save_name, format="wav")

        


        


        
