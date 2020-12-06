
with open("input", 'r') as f:
    lines = f.readlines()

p1_count = 0
p2_count = 0
for line in lines:
    # split password params
    minl, _, rest = line.partition("-")
    maxl, _, rest = rest.partition(" ")
    char, _, rest = rest.partition(":")
    password = rest.strip()
    wcount = password.count(char)

    minl = int(minl)
    maxl = int(maxl)

    if minl <= wcount <= maxl:
        p1_count += 1

    if (password[minl-1] == char) ^ (password[maxl-1] == char):
        p2_count += 1

print(p1_count)
print(p2_count)
