from morse import LETTER_TO_MORSE


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе

    >>> encode('SOS')
    '... --- ...'
    >>> encode('PASHA')
    '.--. .- ... .... .-'
    >>> encode('pasha') # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    KeyError: 'p'
    >>> encode('PAAAAAAAASHA') # doctest: +ELLIPSIS
    '.--. ... .-'
    """
    encoded_signs = [LETTER_TO_MORSE[letter] for letter in message]

    return " ".join(encoded_signs)
