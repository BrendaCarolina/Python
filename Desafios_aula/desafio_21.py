# faça um programa que abra e reproduza um audio mp3

# precisa de uma biblioteca não instalada (pygame - usada para criar jogos + popular)

import pygame
pygame.init()
pygame.mixer.music.load(musica_desejada.mp3) #copiar a musica para a mesma pasta que o programa
pygame.mixer.music.play()
pygame.event.wait()
