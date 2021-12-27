# when normal haptic is not enough
from pynput import keyboard
from arduino import setup
import time

arduino = setup()

def write_read(x):
    arduino.write(bytes(x , 'utf-8'))


def on_press(key):
    print(key)
    if key == keyboard.Key.f12:
        print("Quitting")
        quit()

    write_read('255:0')

def on_release(key):
    write_read('0:0')


    global active

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()

