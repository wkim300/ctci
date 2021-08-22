"""Q1-1"""

import string

def has_unique_chars(input_str):
    """
    Returns a bool whether an input string has all unique characters.
    
    Assumption: all characters are ASCII characters
    """
    # if input larger than allowed ASCII chars, return False
    if len(input_str) > 128:
        return False

    char_exist = [0 for i in range(128)]  # check appeareance

    for char in input_str:
        index = ord(char)
        if char_exist[index]:
            return False
        char_exist[index] = 1
    
    print("All input characters are unique!")
    return True

if __name__=="__main__":
    # Tests
    input_str = "I'm a cat"
    assert has_unique_chars(input_str) == False

    input_str = "You're big"
    assert has_unique_chars(input_str) == True


