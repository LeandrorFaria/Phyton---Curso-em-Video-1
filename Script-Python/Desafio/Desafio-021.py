# Faça um programa em Python que abra e reproduza um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('d-021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
