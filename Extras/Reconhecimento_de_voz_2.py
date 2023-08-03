#Documentação
# https://pypi.org/project/SpeechRecognition/
# https://github.com/cmusphinx/pocketsphinx/blob/master/README.md
# instale a biblioteca
# pip install SpeechRecognition
# pip install pyaudio
# pip install cmake
# pip3 install pocketsphinx
# import pocketsphinx
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio    versão do audio, verificar a sua versão baixar o arquivo e instalar no mesmo diretorio
from pocketsphinx import LiveSpeech

def reconhecer_fala():
    for phrase in LiveSpeech(): 
        print(phrase)
    

reconhecer_fala()
        

