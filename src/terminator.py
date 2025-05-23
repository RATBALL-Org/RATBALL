import socket
import time
from loguru import logger


# Defining Server Parameters
ingestHostIP = "127.0.0.1"
ingestListenerPort = 36783
ingestPort = 36785

# Connecting to Server
ingestSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ingestSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ingestSocket.bind(("127.0.0.1", ingestPort))
ingestSocket.listen()
# ingestSocket.connect((ingestHostIP, ingestListenerPort))
logger.debug("Connected to mock ingestor")

# Defining Peer-to-Peer Server Parameters
jetsonHostIP = "127.0.0.1"
jetsonListenerPort = 36786
jetsonPort = 36787

# Connecting to Peer-to-Peer Server
# jetsonSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# jetsonSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# jetsonSocket.bind(('127.0.0.1', jetsonPort))
# jetsonSocket.connect((jetsonHostIP, jetsonListenerPort))
# logger.log("In programStopClient -- Connected to Jetson!")

# Defining stop message
beginStopMessage = b"BEGIN_STOP"  # Message can be changed, just a prototype

# Waiting to simulate experiment time
numMinutes = 0
numSeconds = 10
time.sleep((60 * numMinutes) + numSeconds)

# Transmitting stop flag
# jetsonSocket.sendall(beginStopMessage)
# logger.log("In programStopClient -- Sent beginStop trigger!")
ingestSocket.close()
# jetsonSocket.close()
