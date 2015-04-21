import zmq
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

context = zmq.Context()

socket = context.socket(zmq.PAIR)
socket.connect("tcp://127.0.0.1:5696")

while True:
    command = str(socket.recv())
    if command == "device_1 ON":
        GPIO.output(7, True)
    if command == "device_1 OFF":
        GPIO.output(7, False)
