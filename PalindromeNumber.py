'''
9. Palindrome Number

https://leetcode.com/problems/palindrome-number/

'''


class Solution:
    def isPalindrome(self, x):

        if x >= 2**31 - 1 or x <= -2**31:
            return False
        num = x
        rev = 0
        while num != 0:
            rev = rev*10 + num % 10
            num = int(num/10)

        return True if rev == x else False


print(Solution().isPalindrome(123121))
