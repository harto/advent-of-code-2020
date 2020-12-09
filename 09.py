with open('inputs/09') as f:
    nums = [int(line.strip()) for line in f]

# window = nums[:25]

# def valid(n):
#     for i in range(len(window)):
#         for j in range(1, len(window)):
#             if window[i] + window[j] == n:
#                 return True
#     return False

# for i in range(len(window), len(nums)):
#     n = nums[i]
#     if not valid(n):
#         print(n)
#         break
#     window = window[1:] + [n]

invalid = 552655238

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
