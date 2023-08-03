#Documentação
# https://pypi.org/project/SpeechRecognition/
# https://github.com/cmusphinx/pocketsphinx/blob/master/README.md
# instale a biblioteca
# pip install SpeechRecognition
# pip install pyaudio
# pip install cmake
# pip3 install pocketsphinx
# import pocketsphinx
from pocketsphinx import LiveSpeech
import speech_recognition as s
'''
speech = LiveSpeech(keyphrase='forward', kws_threshold=1e-20)
for phrase in speech:
    print(phrase.segments(detailed=True))
'''


def reconhecer_fala():
    microfone = s.Recognizer()
    with s.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Pode começar a falar ...")
        audio = microfone.listen(source)
        try:
            #frase = microfone.recognize_google(language='pt-BR')
            #frase = microfone.recognize_google(audio, language='pt-BR')#'pt-BR', 'en-US'
            #frase = microfone.recognize_assemblyai()
            for phrase in LiveSpeech(): 
                print(phrase)
        except s.UnkownValueError:
            print("Não entendi, favor repetir por gentileza !!!")
        return phrase


reconhecer_fala()
        

