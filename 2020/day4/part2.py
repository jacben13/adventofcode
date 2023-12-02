import re

class ByrError(Exception):
    pass

class IyrError(Exception):
    pass

class EyrError(Exception):
    pass

class HgtError(Exception):
    pass

class HclError(Exception):
    pass

class EclError(Exception):
    pass

class PidError(Exception):
    pass

def check_height(hgt):
    units = hgt[-2:]
    measure = int(hgt[:-2])
    if units == 'cm':
        return 150 <= measure <= 193
    elif units == 'in':
        return 59 <= measure <= 76
    else:
        raise Exception


def check_hair_color(hcl):
    return hcl[0] == '#'


def check_eye_color(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def check_pid(pid):
    pattern = r'^[0-9]{9}$'
    return bool(re.match(pattern, pid))


def check_valid(passport):
    try:
        if not 1920 <= int(passport['byr']) <= 2002:
            raise ByrError
        if not 2010 <= int(passport['iyr']) <= 2020:
            raise IyrError
        if not 2020 <= int(passport['eyr']) <= 2030:
            raise EyrError
        if not check_height(passport['hgt']):
            raise HgtError
        if not check_hair_color(passport['hcl']):
            raise HclError
        if not check_eye_color(passport['ecl']):
            raise EclError
        if not check_pid(passport['pid']):
            raise PidError
    except (KeyError, Exception) as e:
        return False

    return True


def create_passport_dict(passport_list):
    passport_dict = {}
    for line in passport_list:
        for pair in line:
            pair_list = pair.split(':')
            passport_dict[pair_list[0]] = pair_list[1]
    return passport_dict


with open('input.txt') as f:
    passport_list = []
    passport_dicts = []
    for line in f:
        if line == '\n':
            passport_dicts.append(create_passport_dict(passport_list))
            passport_list = []
            continue
        line = line.replace('\n', '')
        text = line.split(' ')
        passport_list.append(text)
    passport_dicts.append(create_passport_dict(passport_list))

    valid_passports = 0
    for passport in passport_dicts:
        valid_passports += check_valid(passport)
    print('Valid passports: {} of {} total passports'.format(valid_passports, len(passport_dicts)))