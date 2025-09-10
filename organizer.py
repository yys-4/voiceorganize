import speech_recognition as sr
import os, shutil


def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)
    return r.recognize_google(audio).lower()


def organize_downloads():
    folder = r"C:\Users\ASUS\Downloads"
    for file in os.listdir(folder):
        filepath = os.path.join(folder, file)
        if os.path.isfile(filepath):
            ext = os.path.splitext(file)[1].lower()
            category = "Images" if ext in [".jpg", ".png"] else "Docs"
            target = os.path.join(folder, category)
            os.makedirs(target, exist_ok=True)
            shutil.move(filepath, os.path.join(target, file))


command = listen_command()
if "organize" in command and "downloads" in command:
    organize_downloads()
    print("Files sorted by voice command.")
