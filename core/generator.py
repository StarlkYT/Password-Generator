from random import randint
def generator(length=2, alphabetic=True, numeric=False, special=False):
    """
    Generates a string with the given parameters as options
    :param alphabetic: Adds alphabet letters: A B C...
    :param numeric: Integer numbers only: 1 2 3...
    :param special: Special letters: !@#$%...
    :parameter length: String's length (Maximum 32, Minimum 2)
    :return String:
    """
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    SPECIALS = r"!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
    NUMBERS  = "123456789"

    if 2 <= length <= 32:
        password = ""
        for foo in range(length):
            if alphabetic:
                password += ALPHABET[randint(0, len(ALPHABET) - 1)]
            if numeric:
                password += NUMBERS[randint(0, len(NUMBERS) - 1)]
            if special:
                password += SPECIALS[randint(0, len(SPECIALS) - 1)]
        return password[:length]
    else:
        return False
