'''
7. Reverse Integer

https://leetcode.com/problems/reverse-integer/

'''


class Solution:
    def reverse(self, x: int) -> int:
        neg = False

        if x < 0:
            x = -(x)
            neg = True

        revnum = 0

        while x != 0:
            revnum = revnum*10 + x % 10
            x = int(x/10)

        if neg:
            revnum = -(revnum)

        if revnum >= 2**31-1 or revnum <= -2**31:
            return 0

        return revnum


print(Solution().reverse(1534236469))
