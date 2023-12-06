from math import floor, ceil, sqrt

def resolve(path):
    _total = 1
    _total_2 = 0
    with open(path) as file:
        _times = []
        _distance = []

        for _t in file.readline().split(":")[1].strip().split(" "):
            if _t != "":
                _times.append(int(_t))
        for _t in file.readline().split(":")[1].strip().split(" "):
            if _t != "":
                _distance.append(int(_t))

    # L = t * (T - t) = Tt - t^2
    # L > Lmax if -t^2 + Tt - L > 0
    # get the roof of (-T + sqrt(T^2 - 4L))/-2
    # get the floor of (-T - sqrt(T^2 - 4L))/-2
    for _time, _dist in zip(_times, _distance):
        _delta = sqrt(_time ** 2 - 4 * _dist)

        _first_val = (-_time + _delta)/-2
        _first = ceil(_first_val)
        if _first - _first_val == 0:
            _first = _first + 1

        _second_val = (-_time - _delta)/-2
        _second = floor(_second_val)
        if _second - _second_val == 0:
            _second = _second - 1


        _total *= (_second - _first + 1)

    _total_time = ""
    for _t in _times:
        _total_time += str(_t)
    _total_time = int(_total_time)

    _total_dist = ""
    for _d in _distance:
        _total_dist += str(_d)
    _total_dist = int(_total_dist)

    _time = _total_time
    _dist = _total_dist
    
    _delta = sqrt(_time ** 2 - 4 * _dist)

    _first_val = (-_time + _delta)/-2
    _first = ceil(_first_val)
    if _first - _first_val == 0:
        _first = _first + 1

    _second_val = (-_time - _delta)/-2
    _second = floor(_second_val)
    if _second - _second_val == 0:
        _second = _second - 1


    _total_2 = _second - _first + 1

    return _total, _total_2

print(resolve("./2023/6/input.txt"))
