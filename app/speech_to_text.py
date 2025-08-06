import speech_recognition as sr

recognizer = sr.Recognizer()

def transcribe_microphone_audio():
    with sr.Microphone() as source:
        print("Bir şey söyle, seni dinliyorum...")
        audio = recognizer.listen(source)

    # Google ile tanıma
    try:
        text = recognizer.recognize_google(audio,language="tr-TR")  # Key parametresi ile api anahtarı eklenebilir !!!!!
        print("Duyduğum:", text)
    except sr.UnknownValueError:
        print("Ne dediğini anlayamadım.")
    except sr.RequestError as e:
        print("Google'dan sonuç alınamadı:", e)

if __name__ == "__main__":
    transcribe_microphone_audio()
