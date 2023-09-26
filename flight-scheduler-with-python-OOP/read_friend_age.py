import csv
with open("./data/my_friends .csv", "r") as file:
    lines = csv.reader(file)
    header = next(lines)
    for line in lines:
        if "Bangladesh" in line[0]:
            print(line)
