import re

f = open("../input/04", "r")
one_per_line = [line.rstrip('\n') for line in f]
f.close()

to_validate = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

passports = []

psprt = []
for i in range(len(one_per_line)):
    if i == len(one_per_line)-1:
        psprt += [one_per_line[i]]
        passports.append(psprt)
        psprt = []
    elif one_per_line[i]:
        psprt += [one_per_line[i]]
    elif one_per_line[i] == '':
        passports.append(psprt)
        psprt = []

valid_psprts = 0
for pas in passports:
    valid = True
    for t in to_validate:
        if t not in ",".join(pas):
            valid = False
            break
        else:
            for l in pas:
                for field in l.split(" "):
                    sf = field.split(":")
                    f = sf[0]
                    d = sf[1]

                    if f == "byr":
                        if len(d) != 4 or int(d) < 1920 or int(d) > 2002:
                            valid = False
                            break
                    elif f == "iyr":
                        if len(d) != 4 or int(d) < 2010 or int(d) > 2020:
                            valid = False
                            break
                    elif f == "eyr":
                        if len(d) != 4 or int(d) < 2020 or int(d) > 2030:
                            valid = False
                            break
                    elif f == "hgt":
                        nm = d[:-2]
                        unit = d[-2:]
                        if unit == "cm":
                            if int(nm) < 150 or int(nm) > 193:
                                valid = False
                                break
                        elif unit == "in":
                            if int(nm) < 59 or int(nm) > 76:
                                valid = False
                                break
                        else:
                            valid = False
                            break

                    elif f == "hcl":
                        if not re.fullmatch(r"#[0-9a-f]{6}",d): #TODO try regexp if necessary
                            valid = False
                            break
                    elif f == "ecl":
                        if d not in eye_colors:
                            valid = False
                            break
                    elif f == "pid": #TODO check if all chars are digits if necessary
                        if len(d) != 9:
                            valid = False
                            break


    if valid:
        valid_psprts+=1


print(valid_psprts)
