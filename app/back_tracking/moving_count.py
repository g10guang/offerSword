# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-05 19:47
# 题目描述：https://www.nowcoder.com/practice/6e5207314b5241fb83f2329e89fdecc8?tpId=13&tqId=11219&rp=4&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def movingCount(self, threshold, rows, cols):
        direction = ((-1, 0), (1, 0), (0, 1), (0, -1))
        self.result = 0
        visited = [False] * (rows * cols)

        def move(x, y):
            if 0 <= x < rows and 0 <= y < cols:
                if self.decimalSum(x, y) > threshold:
                    return
                if not visited[cols * x + y]:
                    visited[cols * x + y] = True
                    self.result += 1
                    for m, n in direction:
                        move(x + m, y + n)

        move(0, 0)
        return self.result

    def decimalSum(self, x, y):
        s = 0
        while x:
            x, t = divmod(x, 10)
            s += t
        while y:
            y, t = divmod(y, 10)
            s += t
        return s


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        r = self.s.movingCount(5, 10, 10)
        self.assertEqual(21, r)

    def test_2(self):
        r = self.s.movingCount(15, 100, 1)
        self.assertEqual(79, r)

