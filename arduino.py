import serial
import time

port  = 'COM5' # Adjust this to fit  your setup


# stand by voltate. Motors should have small amount of electricity running through for easy spin up
SMALL_MOTOR_LOW = 13
LARGE_MOTOR_LOW = 13
MAX_VALUE = 255
arduino = None

def setup():
    global arduino
    arduino = serial.Serial(port=port, baudrate=115200,timeout=0.01)
    return arduino

def write_read(value):
    arduino.write(value)

def update_motors(small_motor, large_motor):
    packet = bytearray()
    small_motor = calculate(small_motor, 255,  MAX_VALUE - SMALL_MOTOR_LOW) + SMALL_MOTOR_LOW
    large_motor = calculate(large_motor, 255,  MAX_VALUE - LARGE_MOTOR_LOW) + LARGE_MOTOR_LOW
    
    packet.append(small_motor)
    packet.append(large_motor)
    write_read(packet)


def reset_motors():
    packet = bytearray()
    packet.append(SMALL_MOTOR_LOW)
    packet.append(LARGE_MOTOR_LOW)
    write_read(packet)

def turn_off_motors():
    packet = bytearray()
    packet.append(0)
    packet.append(0)
    write_read(packet)

def clamp(value, min_value, max_value):
    if value <= min_value:
        return min_value
    if value >= max_value:
        return max_value
    return value;

def calculate(value, max_value, max_target):
    percentage = value / max_value;
    return int(percentage * max_target)