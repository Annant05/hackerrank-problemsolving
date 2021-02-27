'''
1. Two Sum

https://leetcode.com/problems/two-sum/

'''


class Solution:
    def twoSum_bruteforce(self, nums, target):
        ''' This version uses brute force for solution '''
        for ext_index in range(0, len(nums)):
            for inter_index in range(ext_index+1, len(nums)):
                if (nums[ext_index] + nums[inter_index]) == target:
                    return [ext_index, inter_index]

    def twoSum_onewayHashTable(self, nums, target):
        ''' This version uses one way hash tables '''
        mymap = {}
        for index, elem in enumerate(nums):
            complement = target - elem
            if (complement in mymap):
                return [mymap.get(complement), index]
            mymap[elem] = index

    def twoSum_twowayHashTable(self, nums, target):
        ''' This version uses two way hash tables '''
        mymap = {elem: index for index, elem in enumerate(nums)}
        print(mymap)

        for index, elem in enumerate(nums):
            complement = target - elem
            if (complement in mymap) and mymap.get(complement) != index:
                return [index, mymap.get(complement)]


nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum_twowayHashTable(nums, target))
