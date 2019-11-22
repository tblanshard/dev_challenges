'''
Your goal is to create a function that removes the first and last letters of a string.
Strings with two characters or less are considered invalid.
You can choose to have your function return null or simply ignore.
'''

def stringPeelerV1(string_to_peel):
    edited = ""
    if len(string_to_peel) <= 2:
        return None
    else:
        for x in range(1, len(string_to_peel) - 1):
            edited += string_to_peel[x]
    return edited

def stringPeelerV2(string_to_peel):
    if len(string_to_peel) > 2:
        return "".join([x for i, x in enumerate(list(string_to_peel)) if (len(string_to_peel) - 1) > i > 0])
    else:
        return None

def stringPeelerV3(string_to_peel):
    return string_to_peel[1:(len(string_to_peel) - 1)] if len(string_to_peel) > 2 else None

print(stringPeelerV3("hello"))
