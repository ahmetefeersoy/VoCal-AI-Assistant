import speech_recognition as sr

recognizer = sr.Recognizer()

def transcribe_microphone_audio():
    with sr.Microphone() as source:
        print("Bir şey söyle, seni dinliyorum...")
        audio = recognizer.listen(source)

    # Google ile tanıma
    try:
        text = recognizer.recognize_google(audio, language="tr-TR")
        return text
    except sr.UnknownValueError:
        print("Ne dediğini anlayamadım.")
        return None
    except sr.RequestError as e:
        print(f"Google'dan sonuç alınamadı: {e}")
        return None