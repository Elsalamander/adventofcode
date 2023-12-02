
def _parse_set(set_data: str) -> dict:
    _result = {}
    for element in set_data.split(","):
        _tmp = element.strip().split(" ")
        _n = int(_tmp[0])
        _color = _tmp[1]
        if _color in _result:
            _result[_color] = _result[_color] + _n
        else:
            _result[_color] = _n
    return _result

def resolve(path, limit):
    _total_1 = 0
    _total_2 = 0
    with open(path) as file:
        for line in file.readlines():
            _data = line.split(":")
            _game_str: str = _data[0]

            _game_number = int(_game_str.split(" ")[1])

            check = True
            _min = {}
            for _set in _data[1].split(";"):
                _set_data = _parse_set(_set.strip())

                for key, value in limit.items():
                    if key in _set_data:
                        if _set_data[key] > value:
                            check = False
                            break
                
                for key, value in _set_data.items():
                    if key in _min:
                        if _min[key] < value:
                            _min[key] = value
                    else:
                        _min[key] = value
                
            if check:
                _total_1 += _game_number

            _tmp = 1
            for key, value in _min.items():
                _tmp *= value
            _total_2 += _tmp

    return _total_1, _total_2

print(resolve("./2023/2/input.txt", {"red": 12, "green": 13, "blue": 14})[0])
print(resolve("./2023/2/input_2.txt", {"red": 12, "green": 13, "blue": 14})[1])
