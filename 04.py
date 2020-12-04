#!/usr/bin/env python

import re

def between(a, b, v):
    try:
        n = int(v or '')
    except ValueError:
        return False
    return a <= n <= b

def valid_height(v):
    m = re.match(r'^([0-9]+)(cm|in)$', v or '')
    if m:
        x, units = m.groups()
        n = int(x)
        return units == 'cm' and 150 <= n <= 193 or units == 'in' and 59 <= n <= 76

def main(inp):
    passports = [
        dict(field.split(':', 2) for field in fields.split())
        for fields in inp.split('\n\n')
    ]

    valid = 0

    for p in passports:
        if between(1920, 2002, p.get('byr')) and \
           between(2010, 2020, p.get('iyr')) and \
           between(2020, 2030, p.get('eyr')) and \
           valid_height(p.get('hgt')) and \
           re.match(r'^#[0-9a-f]{6}$', p.get('hcl', '')) and \
           p.get('ecl') in 'amb blu brn gry grn hzl oth'.split() and \
           re.match(r'^[0-9]{9}$', p.get('pid', '')):
            valid +=1

    print(valid)

if __name__ == '__main__':
    with open('inputs/04') as f:
        main(f.read())
