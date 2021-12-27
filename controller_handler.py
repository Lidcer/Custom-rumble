from keyboard_handle import Keyboard_handle

class Controller_handler:
  def __init__(object, gamepad, keys, controller_key):
      object.gamepad = gamepad
      object.controller_key = controller_key
      object.keyboard_handle = Keyboard_handle(keys);

  def execute(object, incomingKey, value):
    if object.keyboard_handle.can_execute(incomingKey):
        if value == True:
            object.gamepad.press_button(button=object.controller_key)
        else:
            object.gamepad.release_button(button=object.controller_key)
        object.gamepad.update()
        return True
    return False;

maxValue = 32767; 
class Controller_joystick:
    def __init__(object, gamepad, keys, type):
      object.gamepad = gamepad
      object.type = type
      object.x = 0
      object.y = 0
      object.keyboard_handles = [
          Keyboard_handle(keys[0]), # up
          Keyboard_handle(keys[1]), # right
          Keyboard_handle(keys[2]), # down
          Keyboard_handle(keys[3]) # left
          ];
    
    def execute(object, incomingKey, value):
        for index, hander in enumerate(object.keyboard_handles):
            if hander.can_execute(incomingKey):
                if index == 0: # up
                    if value == True:
                        object.y = maxValue
                    else:
                        object.y = 0
                elif index == 1: # right
                    if value == True:
                        object.x = maxValue
                    else:
                        object.x = 0
                elif index == 2: # bottom
                    if value == True:
                        object.y = -maxValue
                    else:
                        object.y = 0
                elif index == 3: # left
                    if value == True:
                        object.x = -maxValue
                    else:
                        object.x = 0

                if object.type == "left":
                    object.gamepad.left_joystick(x_value=object.x, y_value=object.y)
                elif object.type == "right":
                    object.gamepad.right_joystick(x_value=object.x, y_value=object.y)

                object.gamepad.update()
                return True
        return False;