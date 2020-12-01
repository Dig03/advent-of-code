with open("input", 'r') as f:
    lines = [int(line) for line in f.readlines()]

for i in lines:
    if (2020 - i) in lines:
        print(f"p1: {i * (2020 - i)}")
        break

for i in lines:
    for j in lines:
        if (2020 - i - j) in lines:
            print(f"p2: {i * j * (2020 - i - j)}")

