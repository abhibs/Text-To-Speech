from tkinter import *
from tkinter import ttk
from gtts import gTTS
import os

root = Tk()
root.title("Abhiram B S")


def textToSpeech():
    txt = entry.get()
    # language = "kn"  # kannada
    # language = "en"  # english
    # language = "te"  # telegu
    # language = "hi"  # hindi
    language = "ta"  # tamil
    output = gTTS(text=txt, lang=language, slow=True)
    output.save("tamil.mp3")
    os.system("start tamil.mp3")


canvas = Canvas(root, width=400, height=300)
canvas.pack()

label = ttk.Label(root, text="Text To Speech",
                  foreground="blue", font="Arial 30")
canvas.create_window(200, 100, window=label)

entry = ttk.Entry(root)
canvas.create_window(200, 200, window=entry)

btn = ttk.Button(text="Start", command=textToSpeech)
canvas.create_window(200, 250, window=btn)

root.mainloop()
