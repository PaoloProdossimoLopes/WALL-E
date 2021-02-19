import argparse
import os
import queue
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer
import pyaudio
import sys
import pyttsx3 #sintese de fala
import core

#sintese de fala
#engine = pyttsx3.init()

#engine.setProperty('voice', voices[-1].id)

#engine.say("Uuuuaaallyyyye")
#engine.runAndWait()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)


def fala(text):
    engine.say(text)
    engine.runAndWait()


model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4000)
stream.start_stream()


#loop
while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']
            
            print(text)
            #fala(text)#repete oq fala

            if text == "que horas são" or text == "me diga as horas" or text == "fala a hora":
                fala(core.SystemInfo.get_time())