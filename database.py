class Database:
    def __init__(self):
        # We use a dictionary (hash map) to store key-value pairs
        # This is where the data actually lives in RAM
        self.data = {}

    def set(self, key, value):
        # Saves a value
        self.data[key] = value
        return True

    def get(self, key):
        # Retrieves a value. Returns None if key doesn't exist.
        return self.data.get(key)

    def delete(self, key):
        # Deletes a value
        if key in self.data:
            del self.data[key]
            return True
        return False