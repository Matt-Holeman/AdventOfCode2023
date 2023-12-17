from ast import pattern
import time

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

def solve():
    file = open("input.txt")
    recordList = consumeFile(file)
    count = 0
    for record in recordList:
        count +=  findSolutions(record[0], record[1])
    print(f"Final: {count}")

def consumeFile(file):
    recordList = []
    for line in file:
        lineSplit = line.strip().split(' ')
        recordList.append((lineSplit[0], [int(x) for x in lineSplit[1].split(',')]))
    return recordList

# This is an absolute atrocity
def findSolutions(pat, seq):
    length = len(pat)
    count = 0
    for a in range(length):
        if len(seq) == 1:
            if doesMatch(stringifyLayout([a],seq,length), pat):
                count += 1
        else:
            for b in range(a+seq[0]+1, length):
                if len(seq) == 2:
                    if doesMatch(stringifyLayout([a,b],seq,length), pat):
                        count += 1
                else:
                    for c in range(b+seq[1]+1, length):
                        if len(seq) == 3:
                            if doesMatch(stringifyLayout([a,b,c],seq,length), pat):
                                count += 1
                        else:
                            for d in range(c+seq[2]+1, length):
                                if len(seq) == 4:
                                    if doesMatch(stringifyLayout([a,b,c,d],seq,length), pat):
                                        count += 1
                                else:
                                    for e in range(d+seq[3]+1, length):
                                        if len(seq) == 5:
                                            if doesMatch(stringifyLayout([a,b,c,d,e],seq,length), pat):
                                                count += 1
                                        else:
                                            for f in range(e+seq[4]+1, length):
                                                if doesMatch(stringifyLayout([a,b,c,d,e,f],seq,length), pat):
                                                    count += 1
            
    return count

def stringifyLayout(indexes, values, length):
    string = ""
    for i in range(len(indexes)):
        string += f"{"." * (indexes[i]-indexes[i-1]-values[i-1] if i > 0 else indexes[i])}{values[i] * "#"}"
    return string.ljust(length).replace(' ', '.')

def doesMatch(layout, pattern):
    if len(pattern) < len(layout):
             return False
    for i in range(len(layout)):
        if pattern[i] == '#' and layout[i] == '.' or pattern[i] == '.' and layout[i] == '#':
            return False
    return True
            
if __name__ == "__main__":
    main()