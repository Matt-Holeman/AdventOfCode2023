
def main():
    with open("./calibration-input.txt") as file:
        total = 0
        for line in file:
            first = True
            for c in line:
                if c.isdigit():
                    if first:
                        firstNum = c
                        lastNum = c
                    else:
                        lastNum = c
                    first = False
            total += int(f"{firstNum}{lastNum}")
        print(total)

if __name__ == "__main__":
    main()