#!/bin/python3

'''
3. Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''

input_string = "abcabcbb"
# input_string = "bbbbb"
# input_string = "pwwkew"
# input_string = ""


class Solution:
    def lengthOfLongestSubstring(self, s):
        uniq = {}
        longest = 0
        left = 0
        right = 0

        while right < len(s):
            if s[right] not in uniq.keys():
                uniq[s[right]] = right
                longest = max(longest, len(uniq))
                right += 1
            else:
                # print(uniq, s[left])
                uniq.pop(s[left])
                left += 1

        print(uniq, longest)


Solution().lengthOfLongestSubstring(s=input_string)
