def resolve(path):
    _total = 0
    _total_2 = 0
    with open(path) as file:
        _repeat = {}
        for line in file.readlines():
            _data_line = line.split(":")
            _game = int(_data_line[0].split(" ")[-1])
            _data = _data_line[1]
            _winner_str, _number_str = _data.split("|")
            _winner = _winner_str.strip().split(" ")
            _number = _number_str.strip().split(" ")

            _value = 0
            _do = _repeat[_game] + 1 if _game in _repeat else 1
            for _r in range(_do):
                _count_win = 0
                for _n in _number:
                    if _n == "":
                        continue
                    if _n in _winner:
                        if _value == 0:
                            _value = 1
                        else:
                            _value *= 2
                        _count_win += 1
                for i in range(_game + 1, _game + 1 + _count_win):
                    if i in _repeat:
                        _repeat[i] = _repeat[i] + 1
                    else:
                        _repeat[i] = 1
                if _r == 0:
                    _total += _value
                _total_2 += 1
    return _total, _total_2

print(resolve("./2023/4/input.txt"))
