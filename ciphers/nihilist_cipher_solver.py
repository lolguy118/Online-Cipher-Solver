from string import ascii_lowercase as lowercase_letters
from cipher_solver import CipherSolver

class NihilistSolver(CipherSolver):
    def __init__(self) -> None:
        super().__init__()
    
    def encode(self, plaintext, keyword = None) -> str:
        polybius_square = self.get_polybius_key(keyword)

    
    def decode(self, ciphertext, keyword = None) -> str:
        return super().decode(ciphertext, keyword)
    
    def get_polybius_key(self, keyword : str) -> list:
        polybius_square = [[], [], [], [], []]
        keyword_index_left_on = -1
        letters_index_left_on = 0
        for row in polybius_square:
            if len(row) == 5:
                pass
            elif keyword_index_left_on != len(keyword) - 1:
                for index, letter in enumerate(keyword[keyword_index_left_on + 1:]):
                    if not self.letter_is_in_polybius_square(polybius_square, letter):
                        row.append(letter)
                        keyword_index_left_on += 1
                        if len(row) == 5:
                            break
                        else:
                            pass
            if keyword_index_left_on == len(keyword) - 1:
                for index, letter in enumerate(lowercase_letters[letters_index_left_on + 1:]):
                    if not self.letter_is_in_polybius_square(polybius_square, letter):
                        row.append(letter)
                        letters_index_left_on = index
                        if len(row) == 5:
                            break
                        else:
                            pass
        return polybius_square
            
        
    
    def letter_is_in_polybius_square(self, polybius_square : list, letter : str) -> bool:
        for row in polybius_square:
            if letter in row:
                return True
        return False
    
    def get_number_of_letter_in_polybius_square(self, letter : str, polybius_square : list) -> int:
        for index, row in enumerate(polybius_square):
            if letter in row:
                return int(f"{index + 1}" + f"{row.index(letter) + 1}")
        return -1