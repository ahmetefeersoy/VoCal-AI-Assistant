from gtts import gTTS
import os
from TTS.api import TTS

# def speak(text):
#     # Temp klasörünü oluştur
#     temp_folder = "temp"
#     if not os.path.exists(temp_folder):
#         os.makedirs(temp_folder)
    
#     # Ses dosyasını temp klasörüne kaydet
#     temp_file_path = os.path.join(temp_folder, "temp.mp3")
#     tts = gTTS(text=text, lang='tr')  # 'tr' -> Türkçe
#     tts.save(temp_file_path)
    
#     # Ses dosyasını çal
#     os.system(f"afplay {temp_file_path}")  # Mac için ses çalma komutu
# print(TTS.list_models())

# text_to_speech.py
import os
from TTS.api import TTS

# Pick a model explicitly (recommended). Examples:
# English single speaker: tts_models/en/ljspeech/tacotron2-DDC
# Multispeaker English: tts_models/en/vctk/vits
# Turkish: tts_models/tr/common-voice/glow-tts
MODEL_NAME = "tts_models/tr/common-voice/glow-tts"

# If you really want to list models (needs recent TTS version):
# print(TTS.list_models())
# MODEL_NAME = TTS.list_models()[0]

tts = TTS(MODEL_NAME)

kwargs = {}
if hasattr(tts, "speakers") and tts.speakers:
    kwargs["speaker"] = tts.speakers[0]
if hasattr(tts, "languages") and tts.languages:
    kwargs["language"] = tts.languages[0]

text = "Merhaba nasılsınız efendim? Benim adım Vocal Asistan. Size yardımcı olmak amacıyla burdayım? Herhangi bi sorunuz varsa şuan dinliyorum ?"
out_path = "output.wav"
tts.tts_to_file(text=text, file_path=out_path, **kwargs)
os.system(f"afplay {out_path}")