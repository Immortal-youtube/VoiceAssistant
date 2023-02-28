import webbrowser
import speech_recognition as sr
import subprocess
import datetime as dt
import pyttsx3
import os

def speak(text2speak):
    engine = pyttsx3.init()
    engine.say(text2speak)
    engine.runAndWait()


def takeText():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
    except:
        return "Sorry, I didn't hear you."
    return text


if __name__ == "__main__":
    
    speak("Welcome Immortal!")
    if(dt.datetime.now().hour < 12):
        speak("Good Morning!")
    elif(dt.datetime.now().hour < 18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    while True:
    

        finText = takeText().lower()
        if "open discord" in finText:
            subprocess.Popen(
                "C:\\Users\\anshs\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
            speak("Discord is now open!")

        elif "open youtube" in finText:
            webbrowser.open("https://www.youtube.com/")
            speak("Youtube is now open!")

        elif "open google" in finText:
            webbrowser.open("https://www.google.com/")
            speak("Google is now open!")
        
        elif "open stack overflow" in finText:
            webbrowser.open("https://stackoverflow.com/")
            speak("Stackoverflow is now open!")

        elif "open calculator" in finText:
            subprocess.Popen("C:\\Windows\\System32\\calc.exe")
            speak("Calculator is now open!")

        elif "open intellij" in finText:
            subprocess.Popen("C:\\Program Files\\JetBrains\\IntelliJ IDEA 2022.2\\bin\\idea64.exe")
            speak("IntelliJ is now open!")

        elif "open github desktop" in finText:
            subprocess.Popen(
                "C:\\Users\\anshs\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe")
            speak("GitHub Desktop is now open!")

        elif "end python program" in finText:
            speak("Goodbye Immortal!")
            exit()

        elif "open visual studio code" in finText:
            subprocess.Popen(
                "C:\\Users\\anshs\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            speak("Visual Studio Code is now open!")

        elif "open notepad" in finText:
            subprocess.Popen("C:\\Windows\\System32\\notepad.exe")
            speak("Notepad is now open!")

        elif "shut down my computer" in finText:
            speak("Goodbye Immortal! See you soon!")
            os.system("shutdown /s /t 1")

        elif "reboot my computer" in finText:
            speak("rebooting your computer!")
            os.system("shutdown /r /t 1")


        elif "open sql client" in finText:
            subprocess.Popen("C:\\Users\\anshs\\AppData\\Local\\Programs\\arctype\\Arctype.exe")
            speak("Arctype is now open!")

        elif "open word" in finText:
            subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
            speak("Microsoft Word is now open!")
        
        
