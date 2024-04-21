import socket

SERVER_IP = 'localhost'
SERVER_PORT = 5000

def main():
    print("Attempting to connect to the server...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((SERVER_IP, SERVER_PORT))
            print("Connected to server.")
        except Exception as e:
            print(f"Failed to connect to server: {e}")
            return
        
        while True:
            message = input("Enter message (type 'quit' to exit): ")
            if message.lower() == 'quit':
                break
            try:
                sock.sendall(message.encode())
                response = sock.recv(1024).decode()
                print(f"Server says: {response}")
            except Exception as e:
                print(f"Error during communication: {e}")
                break

if __name__ == "__main__":
    main()
