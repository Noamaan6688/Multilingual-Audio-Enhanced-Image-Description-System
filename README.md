# Multilingual Audio Enhanced Image Description System

## 📋 Project Overview  
This project is an **Image-to-Audio Multilingual Object Detection and Description System** that leverages advanced AI models to detect objects in images, describe them, and provide audio output in multiple languages.  
The system uses **Generative AI (Gemini Vision)** for object description, **CLIP Model** for image processing, and **Google Translator** for multilingual translation, with audio output generated using **gTTS (Google Text-to-Speech)**.  

## ✨ Features  
- **Live Camera Capture:** Detect objects using live camera feed.  
- **AI-Powered Descriptions:** Generate detailed descriptions of detected objects.  
- **Multilingual Support:** Translate descriptions into various Indian regional languages like Hindi, Tamil, Kannada, and more.  
- **Audio Output:** Hear translated descriptions in your chosen language.  

## 🛠️ Technologies Used  
- **Google Generative AI (Gemini Vision):** To describe objects in images.  
- **Hugging Face CLIP Model:** For processing and extracting image features.  
- **Deep Translator:** To translate text into various languages.  
- **Google Text-to-Speech (gTTS):** To convert translated text into audio.  
- **OpenCV:** For live camera feed and image capture.  

## 🌟 Supported Languages  
Here are some of the supported Indian regional languages with their codes:  
- **Hindi:** `hi`  
- **Kannada:** `kn`  
- **Tamil:** `ta`  
- **Telugu:** `te`  
- **Malayalam:** `ml`  
- **Gujarati:** `gu`  
- **Marathi:** `mr`  
- **Punjabi:** `pa`  
- **Bengali:** `bn`  

Refer to the full [ISO 639-1 language code list](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for additional languages.  

## 🚀 How to Run  
1. **Clone the Repository:**  
   ```bash  
   git clone https://github.com/Noamaan6688/Multilingual-Audio-Enhanced-Image-Description-System.git  
   cd your-repository-name  
   ```  
2. **Install Dependencies:**  
   Install the required libraries from `requirements.txt`:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. **Set Up API Keys:**  
   - Add your Gemini Vision API key to `utils.py`.  

4. **Run the Application:**  
   ```bash  
   python main.py  
   ```  

5. **Capture Image:**  
   - Press **`C`** to capture an image and process it.  
   - Press **`Q`** to quit the application.  

## 📧 Contact  
For questions or feedback, feel free to reach out:    
**Email:** [noamaan6688@gmail.com]  

## 📜 License  
This project is licensed under the [MIT License](LICENSE).  
