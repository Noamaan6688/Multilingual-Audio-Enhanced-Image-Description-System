import google.generativeai as gai
import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
from gtts import gTTS
import os
from deep_translator import GoogleTranslator

GEMINI_API_KEY='YOUR_GEMINI_API_KEY'
gai.configure(api_key=GEMINI_API_KEY)
model = gai.GenerativeModel('gemini-1.5-flash')
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def detect_objects(frame):
    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    inputs = clip_processor(images=pil_image, return_tensors="pt")
    with torch.no_grad():
        image_features = clip_model.get_image_features(**inputs)
    return "Detected objects are being processed..."

def generate_response(image):
    response = model.generate_content(["Describe the image", image])
    return response.text if response else "No response generated."

def translate_text(text, target_language):
    translation = GoogleTranslator(source='auto', target=target_language).translate(text)
    return translation

def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang)
    filename = "response.mp3"
    tts.save(filename)
    os.system(f'start {filename}')
