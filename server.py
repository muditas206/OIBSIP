import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
names = []


def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode())
        except:
            pass


def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode()

            if message:
                time = datetime.now().strftime("%H:%M")
                index = clients.index(client)
                name = names[index]

                broadcast(f"[{time}] {name}: {message}")
            else:
                remove_client(client)
                break

        except:
            remove_client(client)
            break


def remove_client(client):
    if client in clients:
        index = clients.index(client)
        name = names[index]

        clients.remove(client)
        names.remove(name)
        client.close()

        broadcast(f"{name} has left the chat.")


print("Chat Server Started...")
print("Waiting for clients...")

while True:
    client, address = server.accept()

    client.send("NAME".encode())
    name = client.recv(1024).decode()

    clients.append(client)
    names.append(name)

    print(f"{name} connected from {address}")

    broadcast(f"{name} joined the chat!")

    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()