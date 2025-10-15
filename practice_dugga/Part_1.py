#Part 1

nums = [3,8,0,-2,11,6,6]

def upg_a(nums):
    out = 0
    for num in nums:
        if (num % 2) == 0:
            out += num
    return out


def upg_b(nums):
    out = []
    for num in nums:
        if num >= 0:
            out.append(num**2)
    return out

def upg_c(nums):
    out = set()

    for num in nums:
        if num in out:
            return num
        out.add(num)
    return 'No duplicates'

print(upg_a(nums))
print(upg_b(nums))
print(upg_c(nums))
