from threading import Lock 

class Results:

    def __init__(self):  
        self._lock = Lock()
        self._sent = 0
        self._lost = 0
        self._bytes = 0

    def add_sended(self, byte: int):
        with self._lock:
            self._bytes += byte
            self._sent += 1

    def add_lost(self):
        with self._lock:
            self._lost += 1
    
    def __dict__(self):
        return {
            "sent": self._sent,
            "bytes": self._bytes,
            "lost": self._lost
        }