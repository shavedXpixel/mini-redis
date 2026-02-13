import socket

def run_client():
    # 1. Connect to your running server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('127.0.0.1', 6379))
        print("[*] Connected to Mini-Redis Server")
        
        while True:
            # 2. Ask the user for input
            command = input("mini-redis> ")
            
            if command.lower() == 'exit':
                break
            
            # 3. Send the command to the server
            client.send(command.encode('utf-8'))
            
            # 4. Wait for the server's response
            response = client.recv(1024).decode('utf-8')
            print(f"Server says: {response}")
            
    except ConnectionRefusedError:
        print("Error: Could not connect. Is server.py running?")
    finally:
        client.close()

if __name__ == "__main__":
    run_client()