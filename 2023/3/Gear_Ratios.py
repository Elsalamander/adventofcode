def _add_data(_data, line, column, value):
    if line not in _data:
        _data[line] = {}
    if column in _data[line]:
        _data[line][column]["val"] = _data[line][column]["val"]  * value
        _data[line][column]["count"] = 2
    else:
        _data[line][column] = {"val": value, "count": 1}
        

def resolve(path):
    _total = 0
    _total_2 = 0
    _data = {}
    with open(path) as file:
        lines = file.readlines()
        for index, _line in enumerate(lines):
            line = _line.strip()
            before = lines[index - 1] if index > 0 else None
            after = lines[index + 1] if index < (len(lines) - 1) else None

            _n_start = None
            _n = 0
            _valid = False
            for i, char in enumerate(line):
                if char.isdigit():
                    if _n == 0:
                        _n_start = i
                    _n = _n * 10 + int(char)
                if not char.isdigit() or i == len(line) - 1:
                    if _n > 0:
                        if _n_start > 0 and line[_n_start - 1] != ".":
                            _valid = True
                            if line[_n_start - 1] == "*":
                                _add_data(_data, index, _n_start - 1, _n)
                        elif not line[i].isdigit() and line[i] != ".":
                            _valid = True
                            if line[i] == "*":
                                _add_data(_data, index, i, _n)
                        else:
                            _tmp = _n_start - 1 if _n_start > 0 else _n_start
                            if before:
                                for bf in range(_tmp, i + 1):
                                    if not before[bf].isdigit() and before[bf] != ".":
                                        _valid = True
                                        if before[bf] == "*":
                                            _add_data(_data, index-1, bf, _n)
                            if after:
                                for af in range(_tmp, i + 1):
                                    if not after[af].isdigit() and after[af] != ".":
                                        _valid = True
                                        if after[af] == "*":
                                            _add_data(_data, index+1, af, _n)
                        if _valid:
                            _total += _n
                            _valid = False
                        _n = 0
    for _d in _data.values():
        for _l in _d.values():
            if _l["count"] == 2:
                _total_2 += _l["val"]
    return _total, _total_2

print(resolve("./2023/3/input.txt")[0])
print(resolve("./2023/3/input_2.txt")[1])
