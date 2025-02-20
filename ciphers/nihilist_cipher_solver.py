from string import ascii_lowercase as lowercase_letters
from cipher_solver import CipherSolver

class NihilistSolver(CipherSolver):
    def __init__(self):
        super().__init__()
    
    def encode(self, plaintext, keyword = None):
        return super().encode(plaintext, keyword)
    
    def get_polybius_key(self, keyword : str) -> list:
        polybius_square = [[], [], [], [], []]
        keyword_index_left_on = 0
        letters_index_left_on = 0
        for row in polybius_square:
            if len(row) >= 5:
                pass
            elif keyword_index_left_on != len(keyword) - 1:
                for index, letter in enumerate(keyword[keyword_index_left_on + 1:]):
                    if not self.letter_is_in_polybius_square(polybius_square):
                        row.append(letter)
                        keyword_index_left_on = index
            else:
                for index, letter in enumerate(lowercase_letters[letters_index_left_on + 1:]):
                    if not self.letter_is_in_polybius_square(polybius_square):
                        row.append(letter)
                        letters_index_left_on = index 
            
        
    
    def letter_is_in_polybius_square(self, polybius_square : list, letter : str) -> bool:
        for row in polybius_square:
            if letter in row:
                return True
        return False
        
            