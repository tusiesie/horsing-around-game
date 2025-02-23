import pygame
import os
import sys

class AudioManager:

    def __init__(self):
        # Initialize Pygame mixer
        pygame.mixer.init()

        # # Ser default volumes
        self.volume_levels = {
            "master_volume":.5, 
            "music_volume":.5, 
            "voice_volume":.5
        }

        # Initialize sound directory
        self.audio_file = os.path.join(os.path.dirname(__file__), '../assets/audio')
        current_music_file = os.path.join(self.audio_file, "music/defultBGmusic.mp3")

        # Initialize sound sources
        self.voice_sound = None
        self.music_sound = pygame.mixer.Sound(current_music_file)
        self.music_sound.play(-1)
            

    def get_volume(self, type):
        """
        Get the volume level of given sound type,
        else return default .5
        """
        return self.volume_levels.get(type, .5)

    def set_volume(self, type, value):
        """
        Updates the volume for the given sound type to value
        """
        self.volume_levels[type] = max(0, min(1, value))
        self.recalibrate()

    def recalibrate(self):
        """
        recalibrates volume outputs
        """
        master = self.volume_levels.get("master_volume")
        if self.music_sound:
            self.music_sound.set_volume(self.volume_levels["music_volume"] * master)
        if self.voice_sound:
            self.voice_sound.set_volume(self.volume_levels["voice_volume"] * master)

    def change_music(self, new_file):
        """
        Changes the music with the given filename
        """
        current_music_file = os.path.join(self.audio_file, "music", new_file)
        self.music_sound = pygame.mixer.Sound(current_music_file)
        self.music_sound.play(-1)

    def set_voice_sound(self, type, new_file):
        """
        Sets the current talking voice ("talking") or play once ("sfx")
        """
        current_voice_file = os.path.join(self.audio_file, 'music', new_file)
        self.voice_sound = pygame.mixer.Sound(current_voice_file)

        if (type == "talking"):
            self.voice_sound.play(-1)
        else:
            self.voice_sound.play()
            while self.voice_sound.get_busy():
                for event in pygame.event.get():  # Check for events to keep the window responsive
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
            self.stop_voice_sound()

    def stop_voice_sound(self):
        """
        Stops the playing 
        """
        if self.voice_sound:
            self.voice_sound.stop()
            self.voice_sound = None