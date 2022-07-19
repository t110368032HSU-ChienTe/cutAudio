import secrets
from pydub import AudioSegment
import os

save_folder = "voice1_mergeAudioAudio"
data_folder = "voice1_cutAudio"
cat_sec = 1000



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
        awesome= None
        for wav in wavs:
            
            song = AudioSegment.from_wav(data_folder+'/'+speaker+'/'+wav_name_folder+'/'+wav)
            awesome+=song
        wav_save_name= save_folder+'/'+speaker+'/'+wav_name_folder+'.wav'
        awesome.export(wav_save_name, format="wav")

        


        


        
