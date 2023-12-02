def check_valid(passport):
    # Test set membership for a set containing the keys: byr, iyr, eyr, hgt, hcl, ecl, and pid
    # invalid if missing any of those fields
    #keys_required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    #print('Checking: {}'.format(passport))
    if len(passport.keys()) == 8:
        return True
    elif len(passport.keys()) == 7:
        if 'cid' not in passport.keys():
            return True
        else:
            print('Invalid passport: {}'.format(passport))
            return False
    else:
        print('Invalid passport: {}'.format(passport))
        return False

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