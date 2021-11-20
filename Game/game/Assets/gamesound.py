import pygame
from pygame import mixer

#background music
mixer.music.load("backgroundmusic.mp3")
mixer.music.play(1)

#for when tetrismino moves
#for example
tetrismovekey = mixer.Sound("laser.wav")
tetrismovekey.play()