# if a=1, b=2, c=3, d=4 ... z=26
# then l + o + v + e = 54
# and f + r + i + e + n + d + s + h + i + p = 108
# write a function to find the "strength" of each of these values

def test_calls():
    wordsToMarks("love")
    wordsToMarks("friendship")
    wordsToMarks("attitude")
    wordsToMarks("friends")
    wordsToMarks("family")
    wordsToMarks("selflessness")
    wordsToMarks("knowledge")

def wordsToMarks(word):
    total = 0
    letters = list(word)
    for letter in letters:
        total += (ord(letter) - 96)
    print(total)

test_calls()
