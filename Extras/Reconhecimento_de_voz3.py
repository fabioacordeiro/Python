#Documentação
# https://pypi.org/project/SpeechRecognition/
# https://github.com/cmusphinx/pocketsphinx/blob/master/README.md
# https://letscode.com.br/blog/speech-recognition-com-python
# instale a biblioteca
# pip install SpeechRecognition
# pip install pyaudio
# pip install cmake
# pip3 install pocketsphinx
# import pocketsphinx
#from pocketsphinx import LiveSpeech
import speech_recognition as s

def reconhecer_fala():
    microfone = s.Recognizer()
    with s.Microphone() as source:
        #Ajustando os barulhos para reconhecer melhor a voz
        microfone.adjust_for_ambient_noise(source)
        print("Pode começar a falar ...")
        microfone = microfone.listen(source)
        try:
            frase = microfone.recognize_google(language='pt-BR')
            print(frase)
        except s.UnkownValueError:
            print("Não entendi, favor repetir por gentileza !!!")
        return frase


reconhecer_fala()
        

