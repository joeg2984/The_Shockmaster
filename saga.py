import pygame
import threading
import time

def show_saga():
    # Function to play the MP3 file
    def play_music():
        try:
            pygame.mixer.init()
            pygame.mixer.music.load('sad_violin.mp3')  # Replace with your MP3 file's name
            pygame.mixer.music.play(-1)  # Play in a loop (-1 for infinite looping)
        except Exception as e:
            print("Couldn't play music:", e)
    
    # Start playing the music in a separate thread
    music_thread = threading.Thread(target=play_music)
    music_thread.start()

    # Narrative text with delays
    print("\nThe Saga of The Shockmaster\n")
    time.sleep(4)
    print("Once upon a time, in the world of professional wrestling...")
    time.sleep(3)
    print("A new hero was set to make an earth-shattering debut.")
    time.sleep(3)
    print("Clad in a sparkling stormtrooper helmet and a fur-lined vest...")
    time.sleep(3)
    print("He was The Shockmaster!")
    time.sleep(3)
    print("\nBut fate had other plans.")
    time.sleep(3)
    print("As he burst through the wall...")
    time.sleep(3)
    print("He tripped over a misplaced board...")
    time.sleep(3)
    print("And fell flat on his face, helmet rolling away.")
    time.sleep(3)
    print("\nSilence fell over the arena.")
    time.sleep(2)
    print("Snickers could be heard from his fellow wrestlers.")
    time.sleep(3)
    print("The moment was... shocking, but not in the way anyone expected.")
    time.sleep(3)
    print("\nDetermined to overcome this embarassment,")
    time.sleep(3)
    print("The Shockmaster embarks on a journey of redemption,")
    time.sleep(4)
    print("To prove that he can rise to the top and win the WCW Championship!!")
    time.sleep(5)

    pygame.mixer.music.fadeout(2000)  # Fade out music over 2 seconds
    print("\nThe journey begins now...")
    time.sleep(2)
