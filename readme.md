# Custom rumble

## Requirements
Arduino board that supports 2 pwm outputs
2 sets of vibration motors one should be larger than other 

## Idea
None of keyboards are equipped with vibration motor so I decided to make my own. This python script is emulating virtual gampade control and monitoring when motors are triggered when they are triggered the signal is send to arduino board which activates the vibration motors 

## How to run 
You have to updated script `pi.ino` to your arduino board pins 3, 5 are for the motors they have to support pmw otherwise adjust code.
Check in which USB port your arduino is connected and then adjust arduino.py code

python mockpad.py
<br/>
then press F9 to activate it. This will bind some of the controller keybinding to your keyboard but we aware that you cannot use keyboard in normal way when this is activated.

## Not enough?
python keyboard_haptic.py
<br/>
Should give you haptic feedback on every key press

