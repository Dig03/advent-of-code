with open("input", 'r') as f:
    lines = f.readlines()

# X coordinate loops
# Y coordinate doesn't

def slope_check(lines, dx, dy):
    trees = 0
    # account for newlines
    width = len(lines[0]) - 1
    try:
        x = 0
        y = 0
        while 1:
            x += dx
            y += dy

            if lines[y][x % width] == '#':
                trees += 1
    except IndexError:
        return trees


result = slope_check(lines, 1, 1) * \
         slope_check(lines, 3, 1) * \
         slope_check(lines, 5, 1) * \
         slope_check(lines, 7, 1) * \
         slope_check(lines, 1, 2)


print(result)
