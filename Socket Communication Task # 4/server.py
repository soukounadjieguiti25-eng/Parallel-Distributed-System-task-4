
import socket
import time

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}")

try:
    while True:
        client_socket, client_address = server_socket.accept()

        with client_socket:
            print(f"Connected by {client_address}")

            message = client_socket.recv(1024).decode("utf-8")

            if message:
                print(f"Client message: {message}")
                time.sleep(1)

                response = "Message received"
                client_socket.sendall(response.encode("utf-8"))
                print(f"Response sent: {response}")

            print("Connection closed.\n")

except KeyboardInterrupt:
    print("\nServer stopped.")

finally:
    server_socket.close()
