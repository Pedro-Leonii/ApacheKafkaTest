from dataclasses import dataclass

@dataclass
class SendRequest:
    key: str
    topic: str
    content: bytes
    