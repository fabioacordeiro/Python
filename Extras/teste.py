from pocketsphinx import AudioFile
for phrase in AudioFile("vid.mp3"): 
    print(phrase) 