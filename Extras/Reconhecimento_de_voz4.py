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
    while True:
        microfone = s.Recognizer()
        #microfone.energy_threshold = 300
        #microfone.recognize_ibm="en-US"

        with s.Microphone() as source:
            #Ajustando os barulhos para reconhecer melhor a voz
            microfone.adjust_for_ambient_noise(source)
            print("Pode começar a falar ...")
            audio = microfone.listen(source)
        try:
            #frase = microfone.recognize_google(audio_data=audio, language='en-EU')#'pt-BR'
            frase = microfone.recognize_google(audio, language='pt-BR')#'pt-BR', 'en-US'
            print('Você disse:' + frase)
            if 'Encerrar' in frase:
                break
        except s.UnkownValueError:
            print("Não entendi, favor repetir por gentileza !!!")
        return frase


reconhecer_fala()

print('Reconhecimento de voz fechado...')

