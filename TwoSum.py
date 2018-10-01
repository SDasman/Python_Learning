chicken = [5, 6, 7, 10, 14, 19]
test = [3, 3, 4, 5, 6, 6, 7, 7]
target = 16
testtarget = 14

def twosumv2(nums, target):
    from collections import defaultdict
    difference = defaultdict(list)
    for i in range(0,len(nums)):
        b = target - nums[i]
        difference[b].append(i)
    for key in difference.keys():
        if key*2 == target:
            return difference[key]
        elif key in nums and (target - key) in nums:
            return [nums.index(target-key), nums.index(key)]


print(twosumv2(chicken, target))
print(twosumv2(test, testtarget))
