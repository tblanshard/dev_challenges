def diamond(mid):
    if (mid % 2 == 0) or (mid < 0):
        return None
    else:
        spaces = (mid - 1) // 2
        asterisks = 1
        while asterisks < (mid):
            print((" " * spaces) + ("*" * asterisks) + (" " * spaces))
            spaces -= 1
            asterisks += 2
        spaces = 0
        asterisks = mid
        while asterisks > 0:
            print((" " * spaces) + ("*" * asterisks) + (" " * spaces))
            spaces += 1
            asterisks -= 2

diamond(11)
