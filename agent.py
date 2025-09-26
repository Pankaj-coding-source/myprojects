import speech_recognition as sr
import webbrowser
import pyttsx3
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
if __name__=="__main__":
    speak("initializing agent....")
    recognizer=sr.Recognizer()
    while True:
        with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)
                word = recognizer.recognize_google(audio)
                print("You said:", word)
                word = word.lower()
                if word == "open youtube":
                     speak("opening youtube")
                     webbrowser.open("https://www.youtube.com")
                elif word =="open google":
                     speak("opening google")
                     webbrowser.open("https://www.google.com")
                elif word =="open github":
                     speak("opening github")
                     webbrowser.open("https://www.github.com")
                elif word =="stop":
                     speak("goodbye")
                     break
