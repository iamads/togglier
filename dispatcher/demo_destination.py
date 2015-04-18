import zmq
from optparse import OptionParser


context = zmq.Context()

# Define the socket using the "Context"
socket = context.socket(zmq.PAIR)

# Define the connection using socket command
socket.connect("tcp://127.0.0.1:5696")

socket.send("ajjuakg@gmail.com hello")
socket.send("abhijeet3192@gmail.com hi")

