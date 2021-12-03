from pygame import mixer

#background music
mixer.music.load("backgroundmusic.mp3")
#plays background music infinitely 
mixer.music.play(-1)

#tetrismino move sound
move = mixer.Sound("tetrismovesound.wav")
move.play()