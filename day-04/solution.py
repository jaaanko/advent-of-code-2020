def part1(passports,isValid):
    validPassports = 0

    for passport in passports:
        validPassports += isValid(passport)

    return validPassports

def isValidPart1(passport):
    return len(passport) == 8 or ("cid" not in passport and len(passport) == 7)

def isValidPart2(passport):
    if len(passport) != 8 and ("cid" in passport or len(passport) != 7):
        return False
    
    validByr = len(passport["byr"]) == 4 and 1920 <= int(passport["byr"]) <= 2002
    validIyr = len(passport["iyr"]) == 4 and 2010 <= int(passport["iyr"]) <= 2020
    validEyr = len(passport["eyr"]) == 4 and 2020 <= int(passport["eyr"]) <= 2030
    
    hgtUnit = passport["hgt"][len(passport["hgt"])-2:]
    hgt = passport["hgt"][:len(passport["hgt"])-2]

    if hgtUnit == "cm":
        validHgt = 150 <= int(hgt) <= 193
    elif hgtUnit == "in":
        validHgt = 59 <= int(hgt) <= 76
    else:
        validHgt = False
    
    validHcl = passport["hcl"][0] == "#" and len(passport["hcl"]) == 7

    if validHcl:
        for d in passport["hcl"][1:]:
            if not d.isdigit() and d not in {"a","b","c","d","e","f"}:
                validHcl = False
                break

    validEcl = passport["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    validPid = passport["pid"].isdigit() and len(passport["pid"]) == 9
    
    return validByr and validIyr and validEyr and validHcl and validHgt and validEcl and validPid

with open('input-01.txt') as f:
    passport = {}
    passports = []

    for l in f:
        if l != "\n":
            fields = l.split(" ")
            for f in fields:
                k,v = f.split(":")
                passport[k] = v.rstrip()
        else:
            passports.append(passport)
            passport = {}

    passports.append(passport)

    print(part1(passports,isValidPart1),part1(passports,isValidPart2))