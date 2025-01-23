# Cindy Kuang 
# Homework 7 Question 3
# March 20, 2024
# This program encrypts or decrypts a given text
# using a specified key that is 26 capital letters. 

def translate(from_letters, to_letters, text):
    """
    The translate function does a letter to letter translation.
    The from_letters and to_letters parameters are expected to
    be strings of uppercase letters and both strings need to be 
    the same length. The from_letters and to_letters strings define
    a mapping such that from_letters[i] found in the text string 
    parameter will be converted to to_letters[i].  All characters in 
    the text parameter not found in from_letters are left as-is.
    Case of letters in the text parameter are preserved in the result.
    For example translate("ABC","CAB","C3PO-aBA") will return the 
    string "B3PO-cAC".  Likewise, translate("CAB","ABC","B3PO-cAC")
    will return the string "C3PO-aBA".   
    """

    # Check that parameters meet assumptions. The only assumption not
    # tested is that each character in from_letters should occur once.
    # Students should not change this code.  It is here to catch mistakes.
    if not(from_letters.isupper() and from_letters.isalpha() and 
           to_letters.isupper() and to_letters.isalpha()):
        raise ValueError("from_letters and to_letters must be all uppercase letters")
    if len(from_letters) != len(to_letters):
        raise ValueError("from_letters and to_letters must be the same length")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # Students should add their code below

    translation = ""

    i = 0 
    for i in range(int(len(text))):
        character_to_find = text[i]

        if character_to_find.islower() == True:
            index = from_letters.find(character_to_find.upper())
        else: 
            index = from_letters.find(character_to_find)

        if index != -1: 
            character_mapped = to_letters[index]
            if character_to_find.islower() == True:
                character_mapped = character_mapped.lower()
            translation = translation + character_mapped
        else:
            translation = translation + text[i]
  
    return translation

