import argparse
import os
import queue
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer
import pyaudio
import sys
import pyttsx3 #sintese de fala
import core #comandos

#sintese de fala
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

            # Comando easter egg:
            if text == "quem criou" or text == "criador" or text == "criado" or  text == "criada":
                fala(core.SystemInfo.criador())

            # Comando easter egg:
            if text == "qual é seu nome" or text == "seu nome" or text == "como você se chama" or  text == "quem é voce":
                fala(core.SystemInfo.eu_sou())

            # Comando Hora
            if text == "que horas são" or text == "me diga as horas" or text == "fala a hora":
                fala(core.SystemInfo.get_time())

            # Comando amem
            if text == "oração":
                fala(core.SystemInfo.blessed())

            # Comando dia
            if text == "que dia é hoje" or text == "me diga o dia" or text == "hoje é":
                fala(core.SystemInfo.get_day())