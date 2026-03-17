import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

names = ["Aditya Hulimane" , "Gaurav Bhopi" , "Suraj Baravkar"]

for name in names:
    speaker.Speak(f"Big shoutout to my bro {name}")