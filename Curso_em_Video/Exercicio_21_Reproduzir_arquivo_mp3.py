#Faça um programa para tocar um arquivo mp3 qualquer, no exemplo abaixo utilizamos a biblioteca pygame que é utilizada por jogos
#Esta biblioteca pode ser utilizada para músicas, videos etc.
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('vid2.mp3')
pygame.mixer.music.play()
pygame.event.wait()
