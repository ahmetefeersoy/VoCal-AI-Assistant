from gtts import gTTS
import os

def speak(text):
    # Temp klasörünü oluştur
    temp_folder = "temp"
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    
    # Ses dosyasını temp klasörüne kaydet
    temp_file_path = os.path.join(temp_folder, "temp.mp3")
    tts = gTTS(text=text, lang='tr')  # 'tr' -> Türkçe
    tts.save(temp_file_path)
    
    # Ses dosyasını çal
    os.system(f"afplay {temp_file_path}")  # Mac için ses çalma komutu