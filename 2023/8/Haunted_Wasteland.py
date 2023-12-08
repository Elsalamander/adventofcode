from functools import reduce
from itertools import count
from math import gcd


def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)


class _node(object):
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
    

def _prt(_d):
    _s = ""
    for _a in _d:
        _s += f"{_a.name}, "
    print(_s)

def resolve(path):
    _root = None
    _roots = []
    _tmp_data = {}
    inst = None
    with open(path) as file:
        inst = file.readline().strip()

        file.readline()

        for line in file.readlines():
            _d = line.split("=")
            _name = _d[0].strip()
            _n = _node(_name)
            if _name == "AAA":
                _root = _n
            if _name[2] == "A":
                _roots.append(_n)

            _p = _d[1].strip()[1:-1].split(",")
            _n.left = _p[0].strip()
            _n.right = _p[1].strip()
        
            _tmp_data[_name] = _n

    for _v in _tmp_data.values():
        _v.left = _tmp_data[_v.left]
        _v.right = _tmp_data[_v.right]

    _res_1 = 0
    if _root:
        current = _root
        _cnt = 0
        for _ in count():
            for _i in inst:
                _cnt += 1
                if _i == "R":
                    current = current.right
                elif _i == "L":
                    current = current.left
                if current.name == "ZZZ":
                    _res_1 = _cnt
                    break
            if _res_1 != 0:
                break

    _cnt = 0
    _res_2 = 0
    _current = _roots
    find = {}
    for _i in range(len(_current)):
        find[_i] = 0
    _prt(_current)
    for _ in count():
        for _i in inst:
            _cnt += 1
            for _ic in range(len(_current)):
                if find[_ic] == 0:
                    if _i == "R":
                        _current[_ic] = _current[_ic].right
                    elif _i == "L":
                        _current[_ic] = _current[_ic].left
                    if _current[_ic].name[2] == "Z":
                        find[_ic] = _cnt
            end = True
            for _v in find.values():
                if _v == 0:
                    end = False
            if end:
                _tmp = []
                for _v in find.values():
                    _tmp.append(_v)
                _res_2 = lcm(_tmp)
                break
        if _res_2 != 0:
            break
    
    return _res_1, _res_2

print(resolve("./2023/8/input.txt"))
