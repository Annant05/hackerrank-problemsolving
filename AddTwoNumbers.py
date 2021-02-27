'''
2. Add Two Numbers

https://leetcode.com/problems/add-two-numbers/

'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def generate_input(lis):
    def rec_gen(lis, index):
        if not index:
            return ListNode(lis[index], None)
        return ListNode(lis[index], rec_gen(lis, index - 1))

    return rec_gen(lis, len(lis) - 1)


l1 = generate_input([2, 4, 3])
l2 = generate_input([5, 6, 4])


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        print(l1, l2)


# Solution().addTwoNumbers(l1, l2)


# l1 = [9,9,9,9,9,9]
# l2 = [5, 6, 4]

# l1 = [9, 9, 9, 9, 9, 9, 9]
# l2 = [9, 9, 9, 9]
# Output: [8,9,9,9,0,0,0,1]


l1 = [2, 4, 3]
l2 = [5, 6, 4]


def trynormaladd(l1, l2):
    big_list, small_list = (l1, l2) if (len(l1) >= len(l2)) else (l2, l1)

    res = []
    cflag = 0

    for index in range(len(big_list)):

        sum = cflag

        if(index < len(small_list)):
            sum += small_list[index]

        sum += big_list[index]

        if(sum >= 10):
            cflag = 1
            res.append(sum % 10)
            continue

        cflag = 0
        res.append(sum)

    if cflag:
        res.append(1)

trynormaladd(l1, l2)
