import socket
import threading
from database import Database

# Configuration
HOST = '127.0.0.1'  # Localhost (this computer only)
PORT = 6379         # Standard Redis port

# Initialize our database
db = Database()

def handle_client(client_socket):
    """
    This function runs in a separate thread for EACH user.
    It reads their command, talks to the DB, and sends a response.
    """
    try:
        while True:
            # 1. Receive data from the client (up to 1024 bytes)
            request = client_socket.recv(1024).decode('utf-8')
            
            if not request:
                break # Client disconnected

            # 2. Parse the command (remove whitespace, split by spaces)
            # Example: "SET name gemini" -> ["SET", "name", "gemini"]
            parts = request.strip().split()
            command = parts[0].upper()
            
            response = "ERROR\n"

            # 3. Execute logic based on command
            if command == "SET" and len(parts) >= 3:
                key = parts[1]
                # Join the rest of the parts to allow spaces in value
                value = " ".join(parts[2:]) 
                db.set(key, value)
                response = "OK\n"
            
            elif command == "GET" and len(parts) == 2:
                key = parts[1]
                value = db.get(key)
                if value:
                    response = f"{value}\n"
                else:
                    response = "(nil)\n"

            elif command == "DEL" and len(parts) == 2:
                key = parts[1]
                if db.delete(key):
                    response = "OK\n"
                else:
                    response = "(integer) 0\n"

            # 4. Send the result back to the client
            client_socket.send(response.encode('utf-8'))
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def start_server():
    # 1. Create a TCP/IP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Bind the socket to the address and port
    server.bind((HOST, PORT))
    
    # 3. Listen for incoming connections (max 5 in queue)
    server.listen(5)
    print(f"[*] Server listening on {HOST}:{PORT}")

    while True:
        # 4. Accept a new connection
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        
        # 5. Spin up a new thread to handle this client
        # This allows multiple people to connect at once!
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()