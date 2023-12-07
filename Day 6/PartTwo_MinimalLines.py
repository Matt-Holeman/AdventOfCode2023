file = open("input.txt")
race = (int(file.readline().removeprefix('Time:').replace(' ', '').strip()), int(file.readline().removeprefix('Distance:').replace(' ', '').strip()))
print(sum([(t * (race[0] - t)) > race[1] for t in range(race[0]+1)]))