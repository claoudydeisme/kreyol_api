class TermMemory:
    def __init__(self):
        self.memory = {}

    def register(self, src: str, tgt: str):
        self.memory[src.lower()] = tgt

    def enforce(self, text: str) -> str:
        for src, tgt in self.memory.items():
            text = text.replace(src, tgt)
        return text
