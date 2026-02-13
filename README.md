# Mini-Redis (IronKV)

A custom-built, multi-threaded, in-memory key-value store with persistence, written in Python. This project demonstrates core systems programming concepts including TCP networking, socket programming, concurrency, and file I/O.

## 🚀 Features

* **TCP Server:** Handles raw byte streams over standard sockets.
* **Multi-Threading:** Supports multiple concurrent clients using Python's `threading` module.
* **Persistence:** Implements a write-ahead log style mechanism (JSON based) to save data to disk.
* **Custom Protocol:** Uses a text-based protocol similar to RESP (Redis Serialization Protocol).
* **Graceful Shutdown:** Handles `SIGINT` and ensures data is flushed to disk.

## 🛠️ Architecture

The system consists of three main components:
1.  **Server (`server.py`):** The entry point. Listens on port `6379`, accepts connections, and spawns a new thread for each client.
2.  **Database Engine (`database.py`):** A thread-safe wrapper around a Python dictionary that handles `SET`, `GET`, `DEL` operations and manages disk persistence.
3.  **Client (`client.py`):** A simple REPL (Read-Eval-Print Loop) to interact with the server.

## 📦 Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/mini-redis.git](https://github.com/YOUR_USERNAME/mini-redis.git)
cd mini-redis
```
### 2. Start the Server
Open a terminal and run:
```bash
python server.py
```
You should see: [*] Server listening on 127.0.0.1:6379

### 3. connect with Client
Open a new terminal window and run:
```bash
python client.py
```
## 🎮 Commands
Once connected, you can use the following commands:



#### Command           Description
SET [key] [value] : Stores a key-value pair.
GET [key]         : Retrieves the value of a key.
DEL [key]         : Removes a key.,DEL user
EXIT              : Disconnects from the server.

## 🧪 Technical Details
Language: Python 3

Networking: socket library (AF_INET, SOCK_STREAM)

Concurrency: threading library (Daemon threads)

Persistence: json serialization

---

### Step 2: Commit the README

Go to your terminal and push this update:

```bash
git add README.md
git commit -m "Docs: Added professional README with architecture details"
git push