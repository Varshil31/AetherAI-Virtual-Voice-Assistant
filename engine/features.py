import os
import re
from shlex import quote
import sqlite3
import struct
import subprocess
import webbrowser
import eel
from hugchat import hugchat
from playsound import playsound
import time
import pyaudio
import pyautogui
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
from engine.helper import extract_yt_term, remove_words
import pvporcupine

con = sqlite3.connect("aetherAI.db")
cursor = con.cursor()

@eel.expose
def playAssistantSound():
    music_dir = "www(frontend)/assets/audio/Welcome to AetherAI.mp3"
    time.sleep(0.5)
    playsound(music_dir)


def openCommand(query):
    query = query.replace(ASSISTANT_NAME,  "")
    query = query.replace("open", "")
    query.lower()

    #if query != "":
    #    speak("Opening" + query)
    #    os.system('start' +query)
    #else:
    #    speak("Not opening...")
    app_name = query.strip()
    if app_name != "":
        try:
            cursor.execute("SELECT path FROM sys_command WHERE name IN (?)", (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening" + query)
                os.startfile(results[0][0])
            
            elif len(results) == 0:
                cursor.execute("SELECT url FROM web_command WHERE name IN (?)", (app_name,))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening" + query)
                    webbrowser.open(results[0][0])
                else:
                    speak("Opening" + query)
                    try:
                        os.system('start ' + query)
                    except:
                        speak("Sorry, I am not able to open this application")
        except:
            speak("Sorry, Something went wrong")


def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing" + search_term + " on Youtube")
    kit.playonyt(search_term)


def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    try:
        porcupine = pvporcupine.create(keywords=["jarvis","alexa"])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=porcupine.frame_length)

        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)

            #processing keyword comes from microphone
            keyword_index = porcupine.process(keyword)

            #Checking if keyword is detected
            if keyword_index >= 0:
                speak("Yes, How can I help you?")

                #Listening to the command
                import pyautogui as autogui
                autogui.hotkey('win')
                autogui.press('a')
                time.sleep(2)
                autogui.keyUp('win')

    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

#Find contacts from the database
def findContact(query):    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        if results:
            print(results[0][0])
            mobile_number_str = str(results[0][0])
            if not mobile_number_str.startswith('+91'):
                mobile_number_str = '+91' + mobile_number_str

            return mobile_number_str, query
        else:
            print("Contact not found in database.")
            return 0, ""
    except Exception as e:
        print(f"Error finding contact: {e}")
        speak('not exist in contacts')
        return 0, ""

def whatsApp(mobile_no, message, flag, name):
    print(f"Sending WhatsApp {flag} to {name} ({mobile_no}) with message: {message}")

    if flag == 'message':
        target_tab = 12
        aether_message = "Message sent successfully to " + name
    elif flag == 'call':
        target_tab = 7
        message = ''
        aether_message = "Calling " + name
    else:
        target_tab = 6
        message = ''
        aether_message = "Starting video call with " + name

    # Encode the message for URL
    encoded_message = quote(message)

    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)  # Wait for WhatsApp to open

    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(aether_message)

#chatbot function to get response from hugchat
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine/cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    print(response)
    speak(response)
    return response
