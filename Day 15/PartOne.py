import time

MULT_VALUE = 17

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

def solve():
    file = open("input.txt")
    hashList = consumeFile(file)
    total = 0
    for hashInput in hashList:
        total += hashString(hashInput)
    print(total)

def hashString(inString):
    multiplier = MULT_VALUE
    value = 0
    for c in inString:
        value += ord(c)
        value *= multiplier
        value = value % 256
    return value


def consumeFile(file):
    return file.read().strip().split(',')

if __name__ == "__main__":
    main()