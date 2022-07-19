from pydub import AudioSegment
import os

save_folder = "voice1_cutAudio"
data_folder = "voice1_build"
cat_sec = 60
cat_sec = cat_sec*1000


speakers = os.listdir(data_folder)

for speaker in speakers:
    
    wavs = os.listdir(data_folder+'/'+speaker)
    for wav in wavs:
        if not os.path.exists("{}/{}".format(save_folder,speaker)):
            os.mkdir("{}/{}/{}".format(save_folder,speaker,wav))
        print(wav)
        song = AudioSegment.from_wav(data_folder+'/'+speaker+'/'+wav)
        sec = song.duration_seconds
        rule_times = sec//cat_sec
        rule_times_flout = sec%cat_sec
        #是否低於60s
        if rule_times != 0:
            print("save{}".format(rule_times))
            #每隔60秒切割
            for part in range(rule_times):
                #防止part=0
                part+=1
                time = song[(part-1)*cat_sec:(part)*cat_sec]
                data_split_filename=('{}/{}/{}_{}.wav'.format(save_folder,speaker,wav,part))
                time.export(data_split_filename,format="wav")
        #剩餘部分
        if rule_times_flout!=0:
            time = song[-rule_times_flout:]
            data_split_filename=('{}/{}/{}_{}.wav'.format(save_folder,speaker,wav,'lower_60'))
            time.export(data_split_filename,format="wav")


        


        
