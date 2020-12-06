with open("input", 'r') as f:
    lines = f.readlines()


def parse_line(line):
    return {k: v for k, v in map(lambda s: s.split(':'), line.split())}


REQUIRED_FIELDS = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
}

valid_c = 0

passport = {}
lines.append('\n')
for line in lines:
    passport.update(**parse_line(line))
    # check our current passport is valid
    if line[0] == '\n':
        if REQUIRED_FIELDS.issubset(passport.keys()):
            valid_c += 1
        passport = {}

print(valid_c)
