import speech_recognition as sr
import pyttsx3
from googletrans import Translator

# Initialize Speech Recognition
recognizer = sr.Recognizer()

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

# Initialize Translator
translator = Translator()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble reaching the service.")
        return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

def translate(text, dest_language):
    try:
        translated = translator.translate(text, dest=dest_language)
        return translated.text
    except Exception as e:
        return f"Translation error: {e}"

if __name__ == "__main__":
    speak("Hello! I can be your translator. I can translate to Spanish, Chinese, and french.")
    while True:
        command = listen()
        if "hello" in command:
            speak("Hello! How can I assist you?")
        elif "how are you" in command:
            speak("I'm fine, thank you!")
        elif "bye" in command:
            speak("Goodbye!")
            break
        elif "translate" in command:
            speak("Please say the sentence you want to translate.")
            sentence = listen()
            if "spanish" in command:
                translated_sentence = translate(sentence, 'es')
                speak(f"The translation in Spanish is: {translated_sentence}")
            elif "chinese" in command:
                translated_sentence = translate(sentence, 'zh-cn')
                speak(f"The translation in Chinese is: {translated_sentence}")
            elif "french" in command:
                translated_sentence = translate(sentence, 'fr')
                speak(f"The translation in french is: {translated_sentence}")
            else:
                speak("Sorry, I can only translate to Spanish, Chinese, and Arabic.")
        else:
            speak("Sorry, I didn't understand that command.")
