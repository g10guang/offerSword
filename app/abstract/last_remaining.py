# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-03 13:43
# 题目描述：https://www.nowcoder.com/practice/f78a359491e64a50bce2d89cff857eb6?tpId=13&tqId=11199&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def LastRemaining_Solution(self, n, m):
        """
        思路：使用循环链表解决
        """
        if n <= 0:
            return -1
        if m == 1:
            return n - 1
        head = ListNode(0)
        p = head
        for x in range(1, n):
            p.next = ListNode(x)
            p = p.next
        p.next = head
        p = head
        while p.next != p:
            for _ in range(m - 2):
                p = p.next
            p.next = p.next.next
            p = p.next
        return p.val


class Solution2:
    def LastRemaining_Solution(self, n, m):
        """
        使用动态规划，将原问题转化为规模更小的子问题
        关于约瑟夫环的动态规划解法，原问题与子问题中的下标映射为关键
        """
        if m <= 0:
            return -1
        if n == 0:
            return 1
        else:
            # 子问题中的返回下标与原问题的下标做映射
            return (self.LastRemaining_Solution(n-1, m) + m) % n


class Solution3:
    def LastRemaining_Solution(self, n, m):
        if m <= 0:
            return -1
        s = 0
        for i in range(2, n + 1):
            s = (s + m) % i
        return s


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution2()

    def test_1(self):
        n, m = 5, 3
        r = self.s.LastRemaining_Solution(n, m)
        self.assertEqual(3, r)

    def test_2(self):
        n, m = 0, 0
        r = self.s.LastRemaining_Solution(n, m)
        self.assertEqual(-1, r)

    def test_3(self):
        n, m = 10, 1
        r = self.s.LastRemaining_Solution(n, m)
        self.assertEqual(9, r)
