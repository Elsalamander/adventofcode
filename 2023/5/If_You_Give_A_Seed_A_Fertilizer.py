import time

def resolve(path, second):
    _min = 0
    _seed = None
    _current_map = None
    _keys = []  # only for have the correct order of map
    _maps = {}
    with open(path) as file:
        for line in file.readlines():
            if not _seed:
                _seed = []
                for _s in line.split(":")[1].strip().split(" "):
                    _seed.append(int(_s.strip()))
            elif line.strip() == "":
                continue
            elif "map" in line:
                 _current_map = line
                 _maps[_current_map] = []
                 _keys.append(_current_map)
            else:
                _tmp = []
                for _n in line.strip().split(" "):
                    _tmp.append(int(_n.strip()))
                _maps[_current_map].append(_tmp)

    if second:
        _keep_seed = []
        _mid_seed = None
        for _s in _seed:
            _keep_seed.append(_s)
        _seed.clear()

    _new_seed = []
    _done = False
    while not _done:
        if second:
            _seed.clear()
            _k = 50000000
            print(f"Do {_keep_seed[0]} for next {_keep_seed[1]} {time.time()}")
            if _keep_seed[1] > _k:
                _seed.extend(range(_keep_seed[0], _keep_seed[0] + _k))
                _keep_seed[0] = _keep_seed[0] + _k
                _keep_seed[1] = _keep_seed[1] - _k
            else:
                _seed.extend(range(_keep_seed[0], _keep_seed[0] + _keep_seed[1]))
                _keep_seed.pop(0)
                _keep_seed.pop(0)

        for _key in _keys:
            _new_seed.clear()
            for index, seed in enumerate(_seed):
                _m_list = _maps[_key]
                for _m in _m_list:
                    _s_y = seed - _m[1]
                    if 0 <= _s_y and _s_y < _m[2]:
                        _new_seed.append(_m[0] + _s_y)
                        break
                if len(_new_seed) < index + 1:
                    _new_seed.append(seed)
            _seed.clear()
            for _ns in _new_seed:
                _seed.append(_ns)
        if second:
            if _mid_seed:
                _mid_seed = min(_mid_seed, min(_seed))
            else:
                _mid_seed = min(_seed)
            if len(_keep_seed) == 0:
                _done = True
        else:
            _done = True
    _min = _mid_seed if second else min(_seed)
    return _min

print(resolve("./2023/5/input.txt", False))
print(resolve("./2023/5/input.txt", True))
