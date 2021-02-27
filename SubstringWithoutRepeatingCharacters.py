#!/bin/python3

# URL : https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Sample inputs:
# input_string = "abcabcbb"
# input_string = "bbbbb"
input_string = "pwwkew"
# input_string = ""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        longest = 0
        j = 0
        print(
            f'Before:\n Index: 0 \t Char: "" \t J: {j} \t Longest: {longest} \t Map: {map}')

        for index, character in enumerate(s):
            if character in map:
                j = max(j, map[character] + 1)
            map[character] = index
            longest = max(longest, index - j+1)

            print(
                f'After:\n Index: {index} \t Char: {character} \t J: {j} \t Longest: {longest} \t Map: {map}')

        print(
            f'Final:\n Index: {index} \t Char: {character} \t J: {j} \t Longest: {longest} \t Map: {map}')

        # uniq_dict = {}

        # substring1 = ""
        # substring2 = ""

        # for character in s:
        #     if character not in substring1:
        #         substring1 += character
        #     else:
        #         substring2 += character

        #     if substring1 == substring2:
        #         uniq_dict.add(substring1)
        #         substring1 = ""

        # uniq_dict.append(substring2)
        # # print(f'substring1: {substring1} \nsubstring2: {substring2}')
        # print(f'Uniq List: {uniq_dict}')


Solution().lengthOfLongestSubstring(s=input_string)
