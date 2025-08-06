import json
from text_to_speech import speak
from speech_to_text import transcribe_microphone_audio
from nlp_handler import NLPHandler

def main():
    print("Hoş geldiniz! Sesli asistan başlatılıyor...")
    
    # NLPHandler örneği oluştur
    nlp_handler = NLPHandler()
    
    while True:
        # Speech-to-Text: Kullanıcıdan sesli giriş al
        print("Lütfen konuşun (Çıkmak için 'çıkış' deyin):")
        user_input = transcribe_microphone_audio()
        
        if user_input:
            print(f"Kullanıcıdan alınan metin: {user_input}")
            
        
            if user_input.lower() in ["çıkış", "kapat", "bitir","görüşürüz", "hoşça kal", "güle güle","bay bay", "bye"]:
                print("Asistan kapatılıyor. Görüşmek üzere!")
                speak("Görüşmek üzere , tekrar bekleriz!")
                break
            
            # LLM'e gönder ve yanıt al
            print("Doğal dil işleme yapılıyor...")
            llm_response = nlp_handler.chat.send_message(user_input)
            
            # Yanıtı JSON olarak işle
            try:
                response_json = json.loads(llm_response.text)
                # print(f"LLM'den alınan yanıt: {response_json}")
                
                # JSON'u anlamlı bir metne dönüştür
                if response_json["intent"] == "unknown":
                    response_text = response_json.get("follow_up_question", "Anlaşılamadı.")
                else:
                    response_text = f"{response_json['response_text']}\n" \
                
                # Text-to-Speech: Yanıtı sesli olarak kullanıcıya ilet
                speak(response_text)
            except json.JSONDecodeError:
                print("LLM'den alınan yanıt JSON formatında değil.")
                speak("Bir hata oluştu, lütfen tekrar deneyin.")
        else:
            print("Ses algılanamadı veya bir hata oluştu.")
            speak("Sesinizi algılayamadım, lütfen tekrar eder misiniz ?.")

if __name__ == "__main__":
    main()