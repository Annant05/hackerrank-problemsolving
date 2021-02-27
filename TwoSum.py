'''
1. Two Sum

https://leetcode.com/problems/two-sum/

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ext_index in range(0,len(nums)):
            for inter_index in range(ext_index+1,len(nums)):
                if (nums[ext_index] + nums[inter_index]) == target:
                    return [ext_index, inter_index]