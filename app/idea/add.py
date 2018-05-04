# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-04 12:45
# 题目描述：https://www.nowcoder.com/practice/59ac416b4b944300b617d4f7f111b215?tpId=13&tqId=11201&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    def Add(self, num1, num2):
        """
        python 在位运算方面有点别扭，因为 Python 原生支持大数，也就是不会产生溢出，数值没有固定的位长度
        """
        return sum((num1, num2))


import unittest


class TestCast(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        r = self.s.Add(10, 11)
        self.assertEqual(21, r)

    def test_2(self):
        r = self.s.Add(-1, 2)
        self.assertEqual(1, r)
