
class Monitoring:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Monitoring, cls).__new__(cls)
            cls._messages = []
        return cls._instance
    
    def add_message(self, message: str):
        """Stores the message for later writing."""
        self._messages.append(message)
    
    def write_messages(self):
        """Writes all stored messages, e.g., to a file or console."""
        for message in self._messages:
            print(message)
        self._messages.clear()
