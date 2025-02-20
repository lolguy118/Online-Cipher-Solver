from string import ascii_lowercase as lowercase_letters
from abc import ABC, abstractmethod

class CipherSolver(ABC):
    def __init__(self) -> None:
        self.letters_to_numbers = dict(zip(list(lowercase_letters), [number for number in range(0, 26)]))
        self.multiplicative_inverses =  {1 : 1, 3 : 9, 5: 21, 7 : 15, 9 : 3, 11 : 19, 15 : 7, 17 : 23, 19 : 11, 21 : 5, 23 : 17, 25 : 25}

    @abstractmethod
    def encode(self, plaintext : str, keyword : str = None) -> str:
        pass

    @abstractmethod
    def decode(self, ciphertext : str, keyword : str = None) -> str:
        pass

    def numbers_to_letters(self, number : int) -> str:
        for key, value in self.letters_to_numbers.items():
            if value == number:
                return key