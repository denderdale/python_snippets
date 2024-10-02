# # sound.py
# import pygame
# import os

# class SoundPlayer:
#     def __init__(self, sound_file):
#         self.sound_file = sound_file
#         # Initialize the mixer for playing sounds
#         pygame.mixer.init()

#     def load_music(self):
#         # Ensure the file exists before loading
#         if not os.path.exists(self.sound_file):
#             raise FileNotFoundError(f"The file {self.sound_file} does not exist.")
#         pygame.mixer.music.load(self.sound_file)

#     def play_music(self, loops=0):
#         """Play the loaded sound, with optional looping.
#         loops: -1 for infinite loop, 0 for no loop, or any positive number for a limited loop count."""
#         print(f"Playing sound: {self.sound_file} with loops={loops}")
#         pygame.mixer.music.play(loops=loops)

#     def stop_music(self):
#         # Stop the sound
#         print("Stopping sound.")
#         pygame.mixer.music.stop()


#     def load_and_play_effect(self, effect_file, loops=0):
#         """Play a sound effect in a loop."""
#         if not os.path.exists(effect_file):
#             raise FileNotFoundError(f"The file {effect_file} does not exist.")
        
#         # Load and play the sound effect
#         effect = pygame.mixer.Sound(effect_file)
#         print(f"Playing sound effect: {effect_file} in loop")
#         effect.play(loops=loops)

#     def load_sound(self, effect_file):
#         # Ensure the file exists before loading
#         if not os.path.exists(self.sound_file):
#             raise FileNotFoundError(f"The file {self.sound_file} does not exist.")
#         pygame.mixer.Sound(effect_file)

#     def play_sound(self, loops=0):
#         """Play the loaded sound, with optional looping.
#         loops: -1 for infinite loop, 0 for no loop, or any positive number for a limited loop count."""
#         print(f"Playing sound: {self.sound_file} with loops={loops}")
#         pygame.mixer.music.play(loops=loops)        

# sound.py
import pygame
import os

class SoundPlayer:
    def __init__(self, sound_file=None):
        self.sound_file = sound_file
        self.effect_sound = None
        pygame.mixer.init()

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

    def load_and_play_effect(self, effect_file):
        """Load and play a sound effect."""
        if not os.path.exists(effect_file):
            raise FileNotFoundError(f"The file {effect_file} does not exist.")
        
        # Load the effect sound only once
        if self.effect_sound is None:  
            self.effect_sound = pygame.mixer.Sound(effect_file)
        
        print(f"Playing sound effect: {effect_file}")
        self.effect_sound.play()  # Play the effect sound
