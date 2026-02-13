import json
import os

class Database:
    def __init__(self, filename='db.json'):
        self.filename = filename
        self.data = {}
        # Load data immediately when the database starts
        self.load()

    def set(self, key, value):
        self.data[key] = value
        self.save()  # Auto-save after every write
        return True

    def get(self, key):
        return self.data.get(key)

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self.save()  # Auto-save after delete
            return True
        return False

    def save(self):
        """Writes the current state of data to disk."""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.data, f)
        except Exception as e:
            print(f"[!] Error saving database: {e}")

    def load(self):
        """Reads the database file from disk."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.data = json.load(f)
                print(f"[*] Loaded {len(self.data)} keys from disk.")
            except Exception as e:
                print(f"[!] Error loading database: {e}")
        else:
            print("[*] No existing database found. Starting fresh.")