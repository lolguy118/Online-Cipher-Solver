from cipher_solver import CipherSolver

class NihilistSolver(CipherSolver):
    def __init__(self):
        super().__init__()
    
    def encode(self, plaintext, keyword = None):
        return super().encode(plaintext, keyword)
    
    def get_polybius_key(keyword : str) -> list:
        polybius_key = [[], [], [], [], []]
        for row in polybius_key:
            if len(row) >= 5:
                pass
            