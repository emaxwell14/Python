import socket
print("Started")
comms_socket = socket.socket()
print("Socket")
print(comms_socket)
comms_socket.bind(('127.0.0.1', 50000))
print("Bound")
comms_socket.listen(10)
print("Listening")
connection, address = comms_socket.accept()
print("Running")
print(address)

while True:
    print(connection.recv(4096).decode("UTF-8"))
    send_data = input("Reply: ")
    connection.send(bytes(send_data, "UTF-8"))
    
