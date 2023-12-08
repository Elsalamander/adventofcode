cards = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9":  9,
    "8":  8,
    "7":  7,
    "6":  6,
    "5":  5,
    "4":  4,
    "3":  3,
    "2":  2
}

_point = {
    "five": 7,
    "four": 6,
    "full": 5,
    "three": 4,
    "two pair": 3,
    "one pair": 2,
    "high": 1
}

def _check_point(point, value):
    tmp = 0
    if value == 5:
        tmp = _point["five"]
    elif value == 4:
        tmp = _point["four"]
    elif value == 3:
        if point == 2:
            tmp = _point["full"]
        else:
            tmp = _point["three"]
    elif value == 2:
        if point == 4:
            tmp = _point["full"]
        elif point == 2:
            tmp = _point["two pair"]
        else:
            tmp = _point["one pair"]
    elif value == 1:
        tmp = _point["high"]
    else:
        tmp = 0
    return tmp if tmp > point else point

def _get_hand_point(hand, jolly=False) -> int:
    _d = {}
    for key in cards.keys():
        _d[key] = 0
    for _char in hand:
        _d[_char] = _d[_char] + 1

    _point = 0
    for _k, _v in _d.items():
        if not jolly or (jolly and _k != "J"):
            _point = _check_point(_point, _v)

    if jolly:
        if _point == 6 and _d["J"] == 1:
            _point = 7
        if _point == 4:
            if _d["J"] == 1:
                _point = 6
            if _d["J"] == 2:
                _point = 7
        if _point == 3:
            if _d["J"] == 1:
                _point = 5
        if _point == 2:
            if _d["J"] == 1:
                _point = 4
            if _d["J"] == 2:
                _point = 6
            if _d["J"] == 3:
                _point = 7
        if _point == 1:
            if _d["J"] == 1:
                _point = 2
            if _d["J"] == 2:
                _point = 4
            if _d["J"] == 3:
                _point = 6
            if _d["J"] == 4:
                _point = 7
        if _point == 0:
            _point = 7

    return _point

def _hands_diff(first, second, jolly) -> bool:
    if jolly:
        cards["J"] = 1
    for _f, _s in zip(list(first), list(second)):
        if cards[_f] > cards[_s]:
            cards["J"] = 11
            return True
        elif cards[_f] < cards[_s]:
            cards["J"] = 11
            return False
        else:
            continue
    return False

def _sort(arr, jolly=False):
    n = len(arr)
      
    if n <= 1:
        return
 
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and (key[2] < arr[j][2] or (key[2] == arr[j][2] and not _hands_diff(key[0], arr[j][0], jolly))):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def resolve(path):
    _total = 0
    _total_2 = 0
    hands = []
    hands_2 = []
    with open(path) as file:
        for line in file.readlines():
            _d = line.split(" ")
            hands.append([_d[0], int(_d[1].strip())])
            hands_2.append([_d[0], int(_d[1].strip())])

    for hand in hands:
        hand.append(_get_hand_point(hand[0]))

    for hand in hands_2:
        hand.append(_get_hand_point(hand[0], True))

    _sort(hands)
    _sort(hands_2, True)
    for index, hand in enumerate(hands):
        _total += (index + 1) * hand[1]
    for index, hand in enumerate(hands_2):
        _total_2 += (index + 1) * hand[1]

    return [_total, _total_2]

print(resolve("./2023/7/input.txt"))
