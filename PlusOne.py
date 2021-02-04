#!/bin/python3

# URL : https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits) - 1] += 1
        for index in reversed(range(len(digits))):
            print(f'Index: {index},List: {digits}')
            # print(digits[index])
            if (digits[index] == 10):
                digits[index] = 0
                if(index == 0):
                    digits.insert(0, 1)
                else:
                    digits[index - 1] += 1
        return digits

input_array = [9, 9]

print(
    Solution()
    .plusOne(digits=input_array)
)
