import socket
import threading

HOST = 'localhost'
PORT = 5000
clients = []

def client_thread(conn, addr):
    print(f"Connected by {addr}")
    conn.sendall("Welcome to the chat!".encode())

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            broadcast(data, conn)
        except:
            continue

    conn.close()

def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message)
            except:
                client.close()
                remove(client)

def remove(connection):
    if connection in clients:
        clients.remove(connection)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server is listening on {HOST}:{PORT}...")  # This line confirms the server is ready
        while True:
            conn, addr = server_socket.accept()
            print(f"Connected by {addr}")
            clients.append(conn)
            threading.Thread(target=client_thread, args=(conn, addr)).start()

if __name__ == "__main__":
    main()
