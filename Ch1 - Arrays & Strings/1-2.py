"""Q1-2"""

# Method #2: Check whether character counts are the same
def is_permutation2(str1, str2):
    """
    Returns a bool whether str1 is a permutation of str2
    """
    # if lengths don't match not a permutation
    if len(str1) != len(str2):
        return False

    char_count1 = char_count(str1)
    char_count2 = char_count(str2)
    return char_count1 == char_count2


def char_count(str1):
    char_count = [0 for i in range(128)]  # assume ASCII chars
    for char in str1:
        char_count[ord(char)] += 1  # increment for each appearance
    return char_count


if __name__=="__main__":
    # Tests
    input_str1 = "geeksforgeeks"
    input_str2 = "forgeeksgeeks"
    assert is_permutation2(input_str1, input_str2) == True

    input_str1 = "test"
    input_str2 = "ttew"
    assert is_permutation2(input_str1, input_str2) == False