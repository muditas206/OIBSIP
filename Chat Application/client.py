import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Get name
prompt = client.recv(1024).decode()

if prompt == "NAME":
    name = input("Enter your name: ")
    client.send(name.encode())


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()

            if message:
                print(message)
            else:
                break

        except:
            print("Disconnected from server.")
            break


# Start receiving messages
thread = threading.Thread(target=receive_messages, daemon=True)
thread.start()

print("Connected to chat!")
print("Type your message. Type 'exit' to leave.")

while True:
    message = input()

    if message.lower() == "exit":
        client.close()
        break

    if message.strip():
        try:
            client.send(message.encode())
        except:
            print("Could not send message.")
            break