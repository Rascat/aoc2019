#  range 147981-691423

def check_passwd(number):
    chars = str(number)
     # check adjacent
    if not check_adjacent(chars):
        return False
    if not is_increasing(chars):
        return False
    return True


def check_adjacent(chars):
    for i in range(len(chars) - 1):
        if chars[i] == chars[i + 1]:
            return True
    return False


def is_increasing(chars):
    max_val = 0
    for c in chars:
        val = int(c)
        if val >= max_val:
            max_val = val
        else:
            return False
    return True

possibles = []

for n in range(147981, 691423):
    if check_passwd(n):
        possibles.append(n)

print(len(possibles))

