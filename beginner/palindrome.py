"""Check if a word or phrase is a palindrome by ignoring spaces and capital letters."""


def palindrome(word: str) -> bool:
    """
    LIST COMPREHENSIONS:
    Its a shorted way to write lops to creat list
    [item for item in list condition]
    """
    just_letters_word = "".join([letter for letter in word if letter.isalpha()])
    """
    Checks every letter in the string word and verifies if it is in the alphabet.  
    If it is true, it will be added to the variable.
    """
    just_letters_word = just_letters_word.lower()
    """
    .lower() makes all the characters in a string lowercase.  
    .upper() makes all the characters in a string uppercase.
    """

    reversal_word = just_letters_word[::-1]  # Remember the chain_reversal exercise ;D

    return just_letters_word == reversal_word


if __name__ == "__main__":

    # Ejemplo de uso

    print(palindrome("A man, a plan, acanal, Panama"))  # Resultado: True
    print(palindrome("I am not a cat"))  # Resultado: False
