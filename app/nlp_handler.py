import google.generativeai as genai
import os, sys, json
from dotenv import load_dotenv

# Load the configuration file
with open("../config/berber.json", "r", encoding="utf-8") as file:
    config_data = json.load(file)
    config_info = json.dumps(config_data, ensure_ascii=False, indent=2)

class NLPHandler:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is not set.")
        
        # Config bilgisini role içine formatla
        self.role = f"""
            Sen, VoCal adlı bir sesli asistanın doğal dil işleme (NLP) motorusun. 
            Kullanıcının Türkçe olarak konuştuğu doğal dil girdisini analiz ederek **niyetini (intent)** belirler ve gerekli bilgileri JSON formatında çıkarırsın.
            Config dosyasındaki bilgileri kullanarak kullanıcıya yardımcı olacaksın.

            Config dosyası :
            {config_info}

            ---

            🧾 DÖNDÜRMEN GEREKEN JSON FORMAT

            {{
            "intent": "get_location",
            "service": null,
            "date": null,
            "time": null,
            "duration_minutes": null,
            "customer_name": null,
            "notes": null,
            "response_text": "Kullanıcıya verilecek yanıt metni",
            "follow_up_question": null
            }}

            ---

            🎯 DESTEKLENEN `intent` TİPLERİ VE YANIT ÖRNEKLERİ:

            1. `get_location` - işletmenin yeri
            → "İşletmemiz [config'den konum bilgisi] adresinde bulunuyor."

            2. `get_working_hours` - çalışma saatleri
            → "Çalışma saatlerimiz: [config'den çalışma saatleri]"

            3. `get_services` - sunulan hizmetler
            → "Sunduğumuz hizmetler: [config'den hizmet listesi]"

            4. `create_appointment` - randevu alma
            → Tarih, saat, hizmet bilgilerini topla ve onay ver

            5. `get_availability` - uygun randevu var mı
            → Müsaitlik durumu hakkında bilgi ver

            6. `unknown` - anlaşılmaz ya da desteklenmeyen niyet
            → `follow_up_question` alanına kısa soru yaz

            ---

            🛡️ KURALLAR:
            ✅ `response_text` alanına config dosyasındaki bilgileri kullanarak anlamlı yanıt yaz
            ✅ Randevu alınırken tüm gerekli bilgileri topla
            ✅ Kibar ve profesyonel bir dil kullan
            """
    
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
        self.chat = self.model.start_chat(history=[])

    def generate_text(self, user_input: str) -> str:
        response = self.chat.send_message(user_input)
        return response.text