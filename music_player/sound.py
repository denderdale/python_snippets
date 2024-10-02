# sound.py
import pygame
import os

class SoundPlayer: # default pygame implementation allows 8 channels, can be configured more but if play 9th, it simply overcome channel occupied as first
    def __init__(self, sound_file=None):
        self.sound_file = sound_file
        self.effects = {}  # Dictionary to hold sound effects
        pygame.mixer.init()
        
        # Set the number of channels to 16 (for example)
        pygame.mixer.set_num_channels(16)

    def load_music(self):
        """Load background music."""
        if not os.path.exists(self.sound_file):
            raise FileNotFoundError(f"The file {self.sound_file} does not exist.")
        pygame.mixer.music.load(self.sound_file)

    def play_music(self, loops=0):
        """Play the loaded music."""
        print(f"Playing music: {self.sound_file} with loops={loops}")
        pygame.mixer.music.play(loops=loops)

    def stop_music(self):
        """Stop the music."""
        print("Stopping music.")
        pygame.mixer.music.stop()

    def load_effect(self, effect_name, effect_file):
        """Load a sound effect."""
        if not os.path.exists(effect_file):
            raise FileNotFoundError(f"The file {effect_file} does not exist.")
        
        self.effects[effect_name] = pygame.mixer.Sound(effect_file)  # Load and store the effect
        print(f"Loaded sound effect: {effect_name}")

    def play_effect(self, effect_name):
        """Play a loaded sound effect."""
        if effect_name in self.effects:
            print(f"Playing sound effect: {effect_name}")
            self.effects[effect_name].play()  # Play the effect sound
        else:
            print(f"Sound effect {effect_name} not loaded.")
