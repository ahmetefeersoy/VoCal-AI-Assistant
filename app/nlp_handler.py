import google.generativeai as genai
import os, sys, json
from dotenv import load_dotenv




class NLPHandler:
    role = """
    Sen, VoCal adlı bir sesli asistanın doğal dil işleme (NLP) motorusun. 
    Kullanıcının Türkçe olarak konuştuğu doğal dil girdisini analiz ederek **niyetini (intent)** belirler ve gerekli bilgileri JSON formatında çıkarırsın.

---

🧾 DÖNDÜRMEN GEREKEN JSON FORMAT

{
  "intent": "get_location",         // aşağıda açıklananlardan biri olmalı
  "service": null,
  "date": null,
  "time": null,
  "duration_minutes": null,
  "customer_name": null,
  "notes": null,
  "follow_up_question": null        // intent anlaşılmazsa burada kısa bir soru olacak
}

---

🎯 DESTEKLENEN `intent` TİPLERİ:

1. `create_appointment` - randevu alma  
2. `get_location` - işletmenin yeri  
3. `get_working_hours` - çalışma saatleri  
4. `get_services` - sunulan hizmetler  
5. `get_availability` - uygun randevu var mı  
6. `unknown` - anlaşılmaz ya da desteklenmeyen niyet

---

🛡️ KURALLAR VE GUARDRAILS:

✅ Her zaman sadece **bir intent** döndür.  
✅ Belirsizse `"intent": "unknown"` yaz ve `"follow_up_question"` alanını uygun şekilde doldur.  
✅ Anlaşılan niyetlerde `follow_up_question` değeri **null** olmalı.  
✅ Kullanıcıya yöneltilen soru kısa ve kibar olmalı. (“Ne işlem yaptırmak istediğinizi tekrar eder misiniz?” gibi)

---

📣 ÖRNEKLER

Girdi:
> “Şey ya ben şey için gelecektim aslında, o şey...”

```json
{
  "intent": "unknown",
  "service": null,
  "date": null,
  "time": null,
  "duration_minutes": null,
  "customer_name": null,
  "notes": null,
  "follow_up_question": "Ne işlem yaptırmak istediğinizi biraz daha açık anlatabilir misiniz?"
}

"""
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is not set.")
    
        generation_config = {
            "temperature": 0.3,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "application/json",
        }
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-2.0-flash",
            generation_config=generation_config,
            system_instruction=self.role,
        )
        chat = self.model.start_chat(history=[])
        self.chat=chat

    def generate_text(self, ) -> str:
        response = self.chat.send_message(
            "Kullanıcının Türkçe olarak konuştuğu doğal dil girdisini analiz ederek niyetini belirle ve JSON formatında çıkar",
        )
        return response.text

