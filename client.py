import socket
from threading import Thread
from _thread import start_new_thread

try:
    host = "127.0.0.1"
    port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))

    def message_receive(client_socket):
        while True:
            message_received = client_socket.recv(2048)
            print(f"Server: {message_received.decode('utf-8')}")

    receive = Thread(target=message_receive, args=(client_socket,))
    receive.start()
    while True:
        client_socket.send(input("").encode('utf-8'))
    receive.join()
except KeyboardInterrupt:
    print("Chat termination!!")