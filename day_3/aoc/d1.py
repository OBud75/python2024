left = list()
right = list()

with open("./d1_input.txt") as f:
    for line in f:
        t: list[str] = line.split("   ")
        left.append(t[0])
        right.append(t[1].replace("\n", ""))

print(sum(abs(int(r) - int(l)) for l, r in zip(left.sort(), right.sort())))
