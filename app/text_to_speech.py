from gtts import gTTS
import os
import torch



from TTS.api import TTS
from TTS.utils.manage import ModelManager
from TTS.tts.models.xtts import XttsAudioConfig
torch.serialization.add_safe_globals([XttsAudioConfig])


# MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"
# Alternative single-language Turkish model:
MODEL_NAME = "tts_models/tr/common-voice/glow-tts"
tts = TTS(MODEL_NAME) 
# Print available speakers and languages
print("Available speakers:", tts.speakers)

# tts_instance = TTS()  
# try:
#     manager = ModelManager()
#     models = manager.list_models()
#     # Print each model entry (string or dict depending on version)
#     if isinstance(models, (list, tuple)):
#         for m in models:
#             print(m)
#     else:
#         print(models)
# except Exception as e:
#     print("Model listing failed:", e)

print("Available languages:", getattr(tts, "languages", None))    
kwargs = {}
   
# Prefer Turkish if supported (XTTS supports many languages including Turkish)
langs = getattr(tts, "languages", None)
if langs:
    # Try exact 'tr' first, then any that starts with 'tr'
    if "tr" in langs:
        kwargs["language"] = "tr"
    else:
        tr_like = next((l for l in langs if str(l).lower().startswith("tr")), None)
        if tr_like:
            kwargs["language"] = tr_like

# Pick a default speaker if the model exposes a speakers list
spks = getattr(tts, "speakers", None)
if spks:
    kwargs["speaker"] = spks[0]


def speak(text):
    temp_folder = "temp"
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    
    out_path = os.path.join(temp_folder, "output.wav")
    tts.tts_to_file(text=text, file_path=out_path, **kwargs)
    os.system(f"afplay {out_path}")