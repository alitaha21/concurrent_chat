import socket
from _thread import start_new_thread
from tkinter import Tk, Button, Label, Entry, END

host = "127.0.0.1"
port = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host, port))
server_socket.listen(5)

window = Tk()
window.title("Server side: Chatting")
window.geometry("500x150")

entry = Entry(window, width="83")
entry.grid(row=1 , column=3)

label = Label(window)
label.grid(column=3, row=4)

sessions = []

def submit():
    message = entry.get()
    for i in sessions:
        i.send(message.encode('utf-8'))    
    entry.delete(0, END)    

button = Button(window, width=7, height=1, bg="blue", text="Send", fg="black", command=submit)
button.grid(column = 3,  row = 2)

def receive_thread(client):
    while True:
        message_received = client.recv(2048)
        label["text"] = f"Client: {message_received.decode('utf-8')}"

def main_thread(server_socket):
    while True:
        client_socket, address = server_socket.accept()
        sessions.append(client_socket)

        label["text"] = "New connection from: " + str(address)
        start_new_thread(receive_thread, (client_socket,))
start_new_thread(main_thread, (server_socket,))
window.mainloop()