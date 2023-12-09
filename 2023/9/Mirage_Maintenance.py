def resolve(path):
    _total = 0
    _total_2 = 0
    with open(path) as file:
        for line in file.readlines():
            _data = []
            for _d in line.split(" "):
                _data.append(int(_d))

            _diff = [_data.copy()]
            _current = _data

            _end = False
            _cnt = 1
            while not _end:
                _end = True
                _diff.append([])
                for _i in range(len(_current) - 1):
                    _diff[_cnt].append(_current[_i + 1] - _current[_i])
                    if _diff[_cnt][_i] != 0:
                        _end = False
                _current = _diff[_cnt]
                _cnt += 1

            for _i in range(len(_diff) - 1):
                _li = len(_diff) - 1 - _i
                _lli = _li - 1
                _diff[_lli].append(_diff[_li][-1] + _diff[_lli][-1])

            for _i in range(len(_diff) - 1):
                _li = len(_diff) - 1 - _i
                _lli = _li - 1
                _diff[_lli].insert(0, _diff[_lli][0] - _diff[_li][0])

            _total += _diff[0][-1]
            _total_2 += _diff[0][0]

    return _total, _total_2

print(resolve("./2023/9/input.txt"))
