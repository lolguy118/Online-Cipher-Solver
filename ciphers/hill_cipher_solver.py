from cipher_solver import CipherSolver


class HillCipherSolver(CipherSolver):
    def __init__(self) -> None:
        super().__init__()

    def encode(self, plaintext: str, keyword1 : str = None, keyword2 : str = None) -> str:
        divided_plaintext = self.get_divided_text(plaintext)
        encoding_matrix = self.get_encoding_matrix(keyword1)
        return self.get_final_text(divided_plaintext, encoding_matrix)

    def get_encoding_matrix(self, keyword: str) -> list:
        keyword_matrix = []
        for letter in keyword:
            keyword_matrix.append(self.letters_to_numbers[letter])
        return keyword_matrix

    def decode(self, ciphertext, keyword1 : str = None, keyword2 : str = None) -> str:
        divided_ciphertext = self.get_divided_text(ciphertext)
        decoding_matrix = self.get_decoding_matrix(keyword1)
        return self.get_final_text(divided_ciphertext, decoding_matrix)

    def get_determinant(self, matrix: list) -> int:
        return self.multiplicative_inverses[
            (matrix[0] * matrix[3] - matrix[1] * matrix[2]) % 26
        ]

    def get_inverse(self, matrix: list) -> list:
        copy_of_matrix = matrix
        matrix[0] = copy_of_matrix[3]
        matrix[3] = copy_of_matrix[0]
        matrix[1] = (matrix[1] * -1) % 26
        matrix[2] = (matrix[2] * -1) % 26
        return matrix

    def get_decoding_matrix(self, keyword: str) -> list:
        decoding_matrix = []
        encoding_matrix = self.get_encoding_matrix(keyword)
        determinant = self.get_determinant(encoding_matrix)
        inverse_matrix = self.get_inverse(encoding_matrix)
        for number in inverse_matrix:
            decoding_matrix.append((number * determinant) % 26)
        return decoding_matrix

    def get_divided_text(self, text: str) -> list:
        return [
            self.get_two_by_one_matrix(text[index : index + 2])
            for index in range(0, len(text), 2)
        ]

    def get_two_by_one_matrix(self, letters: list[str, str]) -> list:
        return [
            self.letters_to_numbers[letters[0]],
            self.letters_to_numbers[letters[1]],
        ]

    def get_final_text(
        self, divided_plaintext: list, encoding_or_decoding_matrix: list
    ) -> str:
        final_text = ""
        for first_letter, second_letter in divided_plaintext:
            final_text += self.numbers_to_letters(
                (
                    first_letter * encoding_or_decoding_matrix[0]
                    + second_letter * encoding_or_decoding_matrix[1]
                )
                % 26
            )
            final_text += self.numbers_to_letters(
                (
                    first_letter * encoding_or_decoding_matrix[2]
                    + second_letter * encoding_or_decoding_matrix[3]
                )
                % 26
            )
        return final_text