import socket
import time

HOST = '127.0.0.1'
PORT = 6379
REQUESTS = 10000  # Number of requests to send

def benchmark():
    # 1. Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST, PORT))
        print(f"[*] Connected. Sending {REQUESTS} requests...")
    except ConnectionRefusedError:
        print("[!] Error: Server is not running.")
        return

    # 2. Start the timer
    start_time = time.time()

    # 3. Bombard the server with requests
    for i in range(REQUESTS):
        command = f"SET key{i} value{i}\n"
        s.send(command.encode())
        response = s.recv(1024) # Wait for OK

    # 4. Stop the timer
    end_time = time.time()
    duration = end_time - start_time
    
    # 5. Calculate RPS (Requests Per Second)
    rps = REQUESTS / duration
    
    print(f"\n--- BENCHMARK RESULTS ---")
    print(f"Total Requests: {REQUESTS}")
    print(f"Time Taken:     {duration:.4f} seconds")
    print(f"Throughput:     {rps:.2f} requests/second")
    print(f"-------------------------")
    
    s.close()

if __name__ == "__main__":
    benchmark()