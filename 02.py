#!/usr/bin/env python

import re

def main(lines):
    valid = 0
    for line in lines:
        m = re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
        min_s, max_s, c, password = m.groups()
        min_n = int(min_s)
        max_n = int(max_s)
        # if min_n <= password.count(c) <= max_n:
        #     valid += 1

        c1 = password[min_n-1]
        c2 = password[max_n-1]
        if (c1 == c and c2 != c) or (c1 != c and c2 == c):
            valid += 1
    print(valid)

if __name__ == '__main__':
    with open('inputs/02') as f:
        main(f)
