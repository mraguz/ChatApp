#creating a chat application that should handle the communication between several machines on the same subnet (or perhaps
#transition from this area to a greater one - i.e. to provide the ability to transcend this limitation

#Will start with basic terminal application)
import socket
#constants
#create GUI (shall do last)

#make the communication possible through socket communication
hostName = str()
hostIPAddress = str()
port = 33000  # hardcoded unused port
address = (hostIPAddress, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)

def serverInit():
    global hostName
    global hostIPAddress
    global server
    hostName = socket.gethostname()
    hostIPAddress = socket.gethostbyname(hostName)


def acceptConnections():
    global server
    bufferSize = 1204

    while True:
        connectedSocketObj, clientAddress = server.accept()
        print("%s %s has connected." % clientAddress)
        connectedSocketObj.send(bytes("Greetings from the cave!", "utf8"))
        print("Printing the received message...")
        connectedSocketObj.recv(bufferSize)
        break

    return connectedSocketObj


def sendMessages(connectedSocketObj):

    test_message = "This is test message!"
    connectedSocketObj.send(bytes(test_message, 'utf8'))

    connectedSocketObj.close()

if __name__ == "__main__":
    server.listen(5)

    print("Waiting for connection...")
    serverInit()
    connectedSocketObj = acceptConnections()
    print("Resending the test message")
    sendMessages(connectedSocketObj)

    server.close()
#send messages
#receive messages