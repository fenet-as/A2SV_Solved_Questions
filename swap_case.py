def swap_case(s):
    swapped = ""
    
    for letter in s:
        if letter.islower():
            swapped += letter.upper()
        else:
            swapped += letter.lower()
    
    return swapped
