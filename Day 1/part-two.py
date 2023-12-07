NUMWORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def main():
    file = open("./calibration-input.txt")
    file = file.read()
    total = 0

    for line in iter(file.splitlines()):
        total += returnNumericValue(line)

    print(total)



def returnNumericValue(line):
    first = True
    for i in range(len(line)):      
        c = line[i]
        if c.isdigit():
            if first:
                firstNum = c
                lastNum = c
                first = False
            else:
                lastNum = c
        else: 
            for idx, item in enumerate(NUMWORDS):
                if item in line[i:] and line.index(item, i) == i:
                    num = NUMWORDS.index(item)+1
                    if first:
                        firstNum = num
                        lastNum = num
                        first = False
                    else:
                        lastNum = num
    return int(f"{firstNum}{lastNum}")

if __name__ == "__main__":
    main()