word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def resolve(path) -> int:
    total = 0
    with open(path) as file:
        for line in file.readlines():
            first: str = None
            last: str = None
            for index, char in enumerate(line):
                if char.isdigit():
                    if not first:
                        first = int(char)
                    else:
                        last = int(char)
                else:
                    for i, w in enumerate(word):
                        if len(line) - index >= len(w):
                            if line[index : index + len(w)] == w:
                                if not first:
                                    first = i
                                else:
                                    last = i
                    
            if not last:
                last = first
            total += first * 10 + last
    return total

print(resolve("./2023/1/input.txt"))
print(resolve("./2023/1/input_2.txt"))
