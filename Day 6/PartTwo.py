
def main():
    file = open("input-example.txt")
    raceTuple = consumeFile(file)
    print(raceTuple)
    print(evaluateRace(raceTuple))

def consumeFile(file):
    return (int(file.readline().removeprefix('Time:').replace(' ', '').strip()), int(file.readline().removeprefix('Distance:').replace(' ', '').strip()))

def evaluateRace(race):
    count = 0
    for t in range(race[0]+1):
        count += (t * (race[0] - t)) > race[1]
    return count

if __name__ == "__main__":
    main()