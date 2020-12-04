#!/usr/bin/env python

def part1(nums):
    for i, a in enumerate(nums):
        for j, b in enumerate(nums[i+1:]):
            if a + b == 2020:
                print(a * b)
                return

def part2(nums):
    for i, a in enumerate(nums):
        for j, b in enumerate(nums[i+1:]):
            for k, c in enumerate(nums[j+1:]):
                if a + b + c == 2020:
                    print(a * b * c)
                    return

if __name__ == '__main__':
    with open('inputs/01') as f:
        # part1([int(line.strip()) for line in f])
        part2([int(line.strip()) for line in f])
