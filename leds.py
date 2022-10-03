from pyfirmata import Arduino,SERVO
from time import sleep

port = 'COM3'
board = Arduino(port)

redLed = 8
yeLed = 7
greenLed = 6

board.digital[redLed].write(1)
sleep(2)
board.digital[redLed].write(0)
board.digital[greenLed].write(1)
sleep(2)
board.digital[greenLed].write(0)
board.digital[yeLed].write(1)
sleep(2)
board.digital[yeLed].write(0)
