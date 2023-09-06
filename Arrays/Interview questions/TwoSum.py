class Solution(object):
    def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if num[i] + num[j] == target:
                    return [i,j]
        return []