
from sound import SoundPlayer
import os
import time

if __name__ == "__main__":
    # Set the paths to the sound files
    background_music = os.path.join(os.path.dirname(__file__), 'sound', 'powerful-energy-upbeat.mp3')
    
    # Paths to multiple sound effects
    effects = {
        "pixel_touch": os.path.join(os.path.dirname(__file__), 'sound', 'retro-game-notification-212.wav'),
        "bomb": os.path.join(os.path.dirname(__file__), 'sound', 'game-explosion-echo-1698.wav'),  
        "bonus": os.path.join(os.path.dirname(__file__), 'sound', 'bonus-alert-767.wav'),    
    }

    # Create an instance of SoundPlayer for the background music
    background_player = SoundPlayer(background_music)

    # Load and play the background music
    try:
        background_player.load_music()  # Load the music
        background_player.play_music()   # Play the music

        # Load all sound effects
        effect_player = SoundPlayer()  # No initial sound file
        for effect_name, effect_file in effects.items():
            effect_player.load_effect(effect_name, effect_file)  # Load each sound effect

        # Play a sound effect multiple times (for demonstration)
        effect_player.play_effect("bomb")  # Play notification sound
        for _ in range(30):
            pass
            # effect_player.play_effect("bomb")  # Play notification sound
            # time.sleep(0.1)
            effect_player.play_effect("bomb")  # Play notification sound
            time.sleep(0.1)


            
            


        # Keep the application running to allow the music and effect to play
        input("Press Enter to stop the music and effects...\n")
        
        # Stop both the background music and effect when user interrupts
        background_player.stop_music()  # Stop the music
    except FileNotFoundError as e:
        print(e)
