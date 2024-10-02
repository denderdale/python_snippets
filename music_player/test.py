# main.py
from sound import SoundPlayer
import os
import time

if __name__ == "__main__":
    # Set the paths to the sound files
    background_music = os.path.join(os.path.dirname(__file__), 'sound', 'powerful-energy-upbeat.mp3')
    effect_sound = os.path.join(os.path.dirname(__file__), 'sound', 'retro-game-notification-212.wav')
    effect_sound_2 = os.path.join(os.path.dirname(__file__), 'sound', 'game-explosion-echo-1698.wav')

    

    # Create an instance of SoundPlayer for the background music
    background_player = SoundPlayer(background_music)

    # Load and play the background music
    try:
        background_player.load_music()  # Load the music
        background_player.play_music()   # Play the music

        # Create an instance of SoundPlayer for the sound effect
        effect_player = SoundPlayer('')  # Empty as we will load it later

        # Load the effect sound once
        effect_player.load_and_play_effect(effect_sound_2)  # Load the sound effect

        for n in range(3):
            effect_player.load_and_play_effect(effect_sound_2)  # Play the effect sound
            time.sleep(0.1)  # Delay between plays

        # Keep the application running to allow the music and effect to play
        input("Press Enter to stop the music and effect...\n")
        
        # Stop both the background music and effect when user interrupts
        background_player.stop_music()  # Stop the music
    except FileNotFoundError as e:
        print(e)
