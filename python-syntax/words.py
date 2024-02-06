def print_upper_words(words):
    """
    print each word in uppercase
    For example: 
    >>> print_upper_words(["yes","no","dog","cat"])
    YES
    NO
    DOG
    CAT
    """
    for word in words:
        print(word.upper())

def print_upper_words_start_with_e(words):
    """
    print word to uppercase if it starts with e
    example:
    >>> print_upper_words_start_with_e(["ears","bob","lake","toad"])
    EARS
    """
    for word in words:
        if word.lower().startswith('e'):
            print (word.upper())

def print_upper_words_start_with_letter(words,must_start_with):
    """
    print words that start with inputed letter
    ex:
    >>> print_upper_words_start_with_letter(["yes","no","yellow","red","net","nectar"],must_start_with={"y","r"})
    YES
    YELLOW
    RED
    """
    for word in words:
        for letter in must_start_with:
            if word.lower().startswith(letter.lower()):
                print(word.upper())
               