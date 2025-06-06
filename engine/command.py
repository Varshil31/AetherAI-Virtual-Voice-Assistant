import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    #print(voices)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,10,6)

        try:
            print("Recognizing...")
            eel.DisplayMessage("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            eel.DisplayMessage(query)
            #speak(query)
            time.sleep(2)
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query.lower()
    

@eel.expose
def allCommands(message = 1):
    if message == 1:
        query = takeCommand()
        print(f"Query: {query}")
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    try:
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            message = ""
            contact_no, name = findContact(query)
            print(f"Contact No: {contact_no}, Name: {name}")
            if contact_no != 0:
                if "send message" in query:
                    message = 'message'
                    speak("What message to send?")
                    query = takeCommand()
                    print(f"Message to send: {query}")
                elif "phone call" in query:
                    message = 'call'
                else:
                    message = 'video call'
                
                whatsApp(contact_no, query, message, name)
            else:
                print("Contact not found.")
        else:
            from engine.features import chatBot
            chatBot(query)
            #print("Sorry, I am not able to understand this command.")
    except Exception as e:
        print(f"Sorry, I am not able to understand this command. Error: {e}")

    eel.ShowHood()
    time.sleep(10)