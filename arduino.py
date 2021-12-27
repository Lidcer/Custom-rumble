import serial

port  = 'COM5' # Adjust this to fit  your setup
arduino = None
def setup():
    global arduino
    arduino = serial.Serial(port=port, baudrate=115200)
    return arduino

def write_read(x):
    arduino.write(bytes(x , 'utf-8'))
