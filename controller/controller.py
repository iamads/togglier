import zmq
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

context = zmq.Context()

socket = context.socket(zmq.PAIR)
socket.connect("tcp://127.0.0.1:5696")

gpio_dict = {"device_1": 7, "device_2": 12, "device_3": 15, "device_4": 18}

while True:
    command = str(socket.recv())
    if command == "device_1_ON":
        GPIO.output(gpio_dict["device_1"], True)
    elif command == "device_1_OFF":
        GPIO.output(gpio_dict["device_1"], False)
    elif command == "device_2_ON":
        GPIO.output(gpio_dict["device_2"], True)
    elif command == "device_2_OFF":
        GPIO.output(gpio_dict["device_2"], False)
    elif command == "device_3_ON":
        GPIO.output(gpio_dict["device_3"], True)
    elif command == "device_3_OFF":
        GPIO.output(gpio_dict["device_3"], False)
    elif command == "device_4_ON":
        GPIO.output(gpio_dict["device_4"], True)
    elif command == "device_4_OFF":
        GPIO.output(gpio_dict["device_4"], False)
