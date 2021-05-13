import socket
from _thread import start_new_thread
from threading import Thread

try:
    host = "127.0.0.1"
    port = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))
    server_socket.listen(5)

    def receive_thread(client):
        while True:
            message_received = client.recv(2048)
            print(f"Client: {message_received.decode('utf-8')}")

    def client_thread_function(client):
        receive = Thread(target=receive_thread, args=(client,))
        receive.start()
        while True:
            client.send(input("").encode('utf-8'))
        receive.join()

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from: {address[0]}: {address[1]}")
        start_new_thread(client_thread_function, (client_socket,))
except KeyboardInterrupt:
    print("Chat termination!!")