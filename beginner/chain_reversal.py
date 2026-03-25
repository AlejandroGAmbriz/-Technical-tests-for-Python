"""TODO:
Write a function that takes a string and returns the reversed string.
"""


def chain_reversal(chain_str: str) -> str:
    """SLICING:
    It's a technique to extract parts of a sequence using the "slicing" syntax
    without using explicit loops
    """

    word_reversal = chain_str[::-1]  # -1 to start with the last item

    """
    sequence[start:end:step]

    When any of the parameters are omitted, Python uses their default values:
    
    [0:length of the sequence:1]
    """

    return word_reversal


if __name__ == "__main__":

    # Ejemplo de uso

    print(chain_reversal("Hola Mundo"))  # Resultado: "odnuM aloH"
