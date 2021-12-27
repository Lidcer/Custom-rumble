class Keyboard_handle:
  def __init__(object, keys):
      object.keys = keys;

  def can_execute(object, incomingKey):
    for key in object.keys:
        if key == incomingKey:
            return True
        if hasattr(incomingKey, 'vk') and type(key) == int and incomingKey.vk == key:
            return True
        if hasattr(incomingKey, 'char') and incomingKey.char == key:
            return True
    return False;
