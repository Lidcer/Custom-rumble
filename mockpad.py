import vgamepad as vg
import time
import random
from controller_handler import Controller_handler, Controller_joystick
from pynput import keyboard
from arduino import setup, update_motors, reset_motors, turn_off_motors

test_mode = True;
gamepad = None
x = 0
y = 0
left_x = 0
right_y = 0

listener = None
listener_lock = None
controller_mapper = None;
joystick_handler_left = None;
joystick_handler_right = None;
arduino = setup()

def my_callback(client, target, large_motor, small_motor, led_number, user_data):
    update_motors(small_motor, large_motor)
    #write_read("2" + ":" + str(large_motor))
    #print("work")

def handle_key(key, value):
    global gamepad 
    global controller_mapper 
    global joystick_handler_left 
    global joystick_handler_right 

    if gamepad is None:
        gamepad = vg.VX360Gamepad()
        gamepad.register_notification(callback_function=my_callback)
        controller_mapper = [
            Controller_handler(gamepad, [keyboard.Key.up], vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP),
            Controller_handler(gamepad, [keyboard.Key.down], vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN),
            Controller_handler(gamepad, [keyboard.Key.left], vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT),
            Controller_handler(gamepad, [keyboard.Key.right], vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT),

            Controller_handler(gamepad, [keyboard.Key.space], vg.XUSB_BUTTON.XUSB_GAMEPAD_A),
            Controller_handler(gamepad, [keyboard.Key.shift], vg.XUSB_BUTTON.XUSB_GAMEPAD_B),
            Controller_handler(gamepad, [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r], vg.XUSB_BUTTON.XUSB_GAMEPAD_X),
            Controller_handler(gamepad, [keyboard.Key.alt_l, keyboard.Key.alt_r], vg.XUSB_BUTTON.XUSB_GAMEPAD_Y),

            Controller_handler(gamepad, ["1"], vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB),
            Controller_handler(gamepad, ["3"], vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB),
            Controller_handler(gamepad, ["q"], vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER),
            Controller_handler(gamepad, ["e"], vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER),
            Controller_handler(gamepad, [keyboard.Key.esc], vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK),
            Controller_handler(gamepad, [keyboard.Key.enter], vg.XUSB_BUTTON.XUSB_GAMEPAD_START),
        ]
        joystick_handler_left = Controller_joystick(gamepad, [["w"], ["d"], ["s"], ["a"]], "left")
        joystick_handler_right = Controller_joystick(gamepad, [[104], [102], [98, 101], [100]], "right") # numpad
    
    for handle in controller_mapper:
        if handle.execute(key, value):
            return;


    if joystick_handler_left.execute(key, value) == True:
        return;

    if joystick_handler_right.execute(key, value) == True:
        return;

    if hasattr(key, 'char') == False:
        return

    global x
    global y
    maxValue = 255
    if key.char == "w":
        if value == True:
            y = maxValue
        else:
            y = 0
    if key.char == "s":
        if value == True: 
            y = -maxValue
        else:
            y = 0

    if key.char == "a":
        if value == True:
            x = maxValue
        else:
            x = 0
    if key.char == "d" or key == keyboard.Key.right:
        if value == True: 
            x = -maxValue
        else:
            x = 0

    check1 = key.char == "w" or key.char == "s"
    check2 = key.char == "a" or key.char == "d"
    if check1 == True or check2 == True:
        gamepad.left_joystick(x_value=x, y_value=y)
        gamepad.update()


def on_press(key):
    return handle_key(key, True)

def on_release(key):
    if on_lock_press(key) == False:
        return False
    return handle_key(key, False)

# with keyboard.Listener(
#         suppress=True,
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()



def create_lock():
    global listener_lock
    global listener
    if listener_lock is not None:
        listener_lock.stop()
        listener_lock = None
    if listener is not None:
        listener.stop()

    listener_lock = keyboard.Listener(on_release=on_lock_press)
    listener_lock.start()
    listener_lock.join()


def kill_all_listiners():
    kill_listener_lock()
    kill_listener()


def kill_listener_lock():
    global listener_lock
    if listener_lock is not None:
        listener_lock.stop()
        listener_lock = None

def kill_listener():
    global listener
    if listener is not None:
        listener.stop()
        listener = None

def create_listener_lock():
    kill_all_listiners()
    global listener_lock
    listener_lock = keyboard.Listener(on_release=on_lock_press)
    listener_lock.start()
    listener_lock.join()

def create_listener():
    kill_all_listiners()
    global listener
    listener = keyboard.Listener(suppress=True,on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()
    print("test")


def notify():
    update_motors(255, 0)
    time.sleep(0.25)
    update_motors(0, 0)

def on_lock_press(key):
    global listener
    global listener_lock


    if key == keyboard.Key.f12:
        turn_off_motors()
        print("Quitting")
        quit()

    if test_mode == True:
        if key == keyboard.Key.f8 or key == keyboard.Key.f7:
            motor = '1'
            if key == key == keyboard.Key.f7:
                motor = '2'

            time.sleep(0.5)
            update_motors(0, 0)
            time.sleep(0.5)
            update_motors(128, 0)
            time.sleep(0.5)
            update_motors(255, 0)
            time.sleep(0.5)
            update_motors(0, 0)
            time.sleep(0.5)

    if key == keyboard.Key.f9:
        if listener is None:
            print("Enable")
            notify()
            create_listener()
        else:
            print("Disabled")
            notify()
            turn_off_motors()
            create_listener_lock()
            return False


create_listener_lock()