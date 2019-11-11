# if a=1, b=2, c=3, d=4 ... z=26
# then l + o + v + e = 54
# and f + r + i + e + n + d + s + h + i + p = 108
# write a function to find the "strength" of each of these values

from functools import reduce

def test_calls():
    wordsToMarks("love")
    wordsToMarks("friendship")
    wordsToMarks("attitude")
    wordsToMarks("friends")
    wordsToMarks("family")
    wordsToMarks("selflessness")
    wordsToMarks("knowledge")

#my initial solution
def wordsToMarksv1(word):
    total = 0
    letters = list(word)
    for letter in letters:
        total += (ord(letter) - 96)
    print(total)

#my improved solution
def wordsToMarks(word):
    print(reduce((lambda x,y: x+y), map((lambda x: ord(x) - 96), list(word))))

test_calls()
