
import socket

HOST = "127.0.0.1"
PORT = 5000

print("=== Simple Messaging Client ===")
print("Type 'exit' to stop the client.")

while True:
    message = input("\nEnter your message: ")

    if message.lower() == "exit":
        print("Client stopped.")
        break

    if not message.strip():
        print("Please enter a non-empty message.")
        continue

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            client_socket.sendall(message.encode("utf-8"))

            response = client_socket.recv(1024).decode("utf-8")
            print(f"Server response: {response}")

    except ConnectionRefusedError:
        print("Cannot connect. Make sure the server is running.")
        break
