import cv2
from utils import detect_objects, generate_response, translate_text, text_to_speech
from PIL import Image

def main():
    target_language = 'en' 
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame from camera. Exiting...")
            break

        if cv2.waitKey(1) & 0xFF == ord('c'): 
            pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            response = generate_response(pil_image)
            print("Assistant:", response)

            translated_response = translate_text(response, target_language)
            print("Translated Assistant:", translated_response)

            text_to_speech(translated_response, lang=target_language)

        cv2.imshow('Live Object Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
