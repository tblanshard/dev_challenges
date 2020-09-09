def vowelCounter(stringToCount):
    counter = 0
    for letter in stringToCount:
        if letter.lower() in ['a','e','i','o','u']:
            counter += 1
    return counter

import re

def vowelCounterImproved(stringToCount):
    return len(re.findall(r'[aeiou]', stringToCount.lower()))

print(vowelCounterImproved("abcdeA"))
