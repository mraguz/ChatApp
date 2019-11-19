import socket

hostServer = "192.168.5.11"
portServer = 33000
bufferSize = 1024
serverAddress = (hostServer, portServer)
clientSocket = socket.socket()

#clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#clientSocket.connect(serverAddress)

def clientInit():
    global clientSocket
    global hostServer
    global portServer
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(serverAddress)

def receiveMessages():
    global clientSocket
    global bufferSize
    while True:
        try:
            message = clientSocket.recv(bufferSize).decode("utf8")
            print(message)
            break
        except Exception as e:
            print("Error is: {}".format(e))
    #clientSocket.close()


def sendMessages():
    global clientSocket
    test_message = "This is test message!"
    clientSocket.send(bytes(test_message, 'utf8'))
    clientSocket.close()


if __name__ == "__main__":
    clientInit()
    receiveMessages()
    print("Sending the message...")
    sendMessages()

