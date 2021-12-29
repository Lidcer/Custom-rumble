# when normal haptic is not enough
from pynput import keyboard
from arduino import setup, update_motors, reset_motors, turn_off_motors
import time

arduino = setup()

def on_press(key):
    print(key)
    if key == keyboard.Key.f12:
        turn_off_motors()
        print("Quitting")
        quit()
    update_motors(128, 0)

def on_release(key):
    reset_motors()

    global active

reset_motors()
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()

