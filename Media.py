import vosk 
import json
from pydub import AudioSegment
import subprocess
import os

def audio_rec(path):
    #loads_model
    model = vosk.Model('H://MyCode//UserBotForAlice//UserBotForAlice//vosk_model')

    print(path)

    #converts audio into wav
    try:
        file_path_wav = 'H://MyCode//UserBotForAlice//UserBotForAlice//new.wav'
        command = ['H://MyCode//UserBotForAlice//UserBotForAlice//ffmpeg-2024-07-04-git-03175b587c-full_build//bin//ffmpeg.exe', "-i", path, "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "2", file_path_wav]

        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print("Ошибка при конвертировании аудио:", e)

    rec = vosk.KaldiRecognizer(model, 16000)
    rec.SetWords(True)

    ogg = AudioSegment.from_wav(file_path_wav)
    ogg = ogg.set_channels(1)
    ogg = ogg.set_frame_rate(16000)

    rec.AcceptWaveform(ogg.raw_data)
    result = json.loads(rec.Result())

    os.remove('H://MyCode//UserBotForAlice//UserBotForAlice//new.wav')

    return result['text']