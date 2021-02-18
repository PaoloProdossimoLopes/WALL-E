#main code
import speech_recognition as sr

#create a recognazer
r = sr.Recognizer()

#open mic to recorder
with sr.Microphone() as source:
    audio = r.listen(source) #define a fonte de audio como microfone

    print(r.recognize_google())