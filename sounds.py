from pygame import mixer
import os

class Music:
    def __init__(self):
        mixer.init()
        print("Current working directory:", os.getcwd())
        print("Content of the current directory:", os.listdir())
        self.bg_music = mixer.Sound('Sounds/bg_sound.mp3')
        self.apple_droped = mixer.Sound('Sounds/apple_dropped.mp3')
        self.apple_catched = mixer.Sound('Sounds/apple_catched.mp3')
        self.game_over = mixer.Sound('Sounds/game_over.mp3')
