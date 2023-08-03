#Documentação
# https://pypi.org/project/SpeechRecognition/
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio biblioteca o audio verificar a sua versão e instalar via cmd informando o caminho completo do local onde baixou o arquivo
# instale a biblioteca
# Vídeo como criar o seu próprio assistente virtual com Python em
# pip install SpeechRecognition
# pip install pyaudio
# pip install vosk (caso não conseguir e aparecer a mensagem de erro abaixo siga os passos a seguir:)
# Error [WinError 225] Não foi possível concluir a operação com êxito porque o arquivo contém um vírus ou software possivelmente indesejado while executing command python setup.py egg_info
# 1) Abra no Windows/Configurações do Windows/Proteção contra vírus e ameaças/App
# RAV Endpoint Protection/Proteção/Ativar proteção em tempo real (Desabilitar por 10 minutos)
# pip install cmake
# 2) Abrao cmd e instale o vosk novamente (pip install vosk)
# Agora vamos acessar a biblioteca de modelos de qual linguagem deseja implementar no endereço abaixo
# https://alphacephei.com/vosk/models
# 
#from pocketsphinx import LiveSpeech
import speech_recognition as sr

# Cria um reconhecedor
r = sr.Recognizer()

# Abrir o microfone para captura
with sr.Microphone() as source:
    while True:
        print('Pode começar a falar ...')
        audio = r.listen(source) # Define microfone como fonte de aúdio
        print(r.recognize_google(audio, language='pt-BR'))



'''
#reconhecer_fala():
    while True:
        microfone = sr.Recognizer()
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

'''