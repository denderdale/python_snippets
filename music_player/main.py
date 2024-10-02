# main.py
from sound import SoundPlayer
import os
import time

if __name__ == "__main__":
    # Set the paths to the sound files
    background_music = os.path.join(os.path.dirname(__file__), 'sound', 'powerful-energy-upbeat.mp3')
    effect_sound = os.path.join(os.path.dirname(__file__), 'sound', 'retro-game-notification-212.wav')

    # Create an instance of SoundPlayer for the background music
    background_player = SoundPlayer(background_music)
    effect_player = SoundPlayer(effect_sound)


    # Load and play the background music
    try:
        background_player.load_music()
        background_player.play_music()

        

        for n in range(10):
            effect_player = SoundPlayer('')
            effect_player.load_and_play_effect(effect_sound, loops=0)
            time.sleep(0.1)


        # Keep the application running to allow the music and effect to play
        input("Press Enter to stop the music and effect...\n")
        
        # Stop both the background music and effect when user interrupts
        background_player.stop_music()
    except FileNotFoundError as e:
        print(e)


    # try:
    #     background_player.load_sound()
    #     background_player.play_sound()

    #     # Load the effect sound once
    #     effect_player.load_sound()  # Load the effect sound

    #     for n in range(10):
    #         effect_player.play_sound(loops=0)  # Play the effect sound
    #         time.sleep(0.1)

    #     # Keep the application running to allow the music and effect to play
    #     input("Press Enter to stop the music and effect...\n")
        
    #     # Stop both the background music and effect when user interrupts
    #     background_player.stop_sound()
    # except FileNotFoundError as e:
    #     print(e)        
