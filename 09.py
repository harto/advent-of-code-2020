with open('inputs/09') as f:
    nums = [int(line.strip()) for line in f]

for i in range(25, len(nums)):
    n = nums[i]
    if not any(nums[j] + nums[k] == n
               for j in range(i - 25, i)
               for k in range(j + 1, i)):
        invalid = n
        print(n)
        break

i = 0
j = 2

while sum(nums[i:j]) != invalid:
    if sum(nums[i:j]) < invalid:
        j += 1
    else:
        i += 1
        if j - i < 2:
            j = i + 2

print(min(nums[i:j]) + max(nums[i:j]))
