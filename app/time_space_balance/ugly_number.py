# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-02 10:08
# 题目描述：https://www.nowcoder.com/practice/6aa9e04fc3794f68acf8778237ba065b?tpId=13&tqId=11186&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    def GetUglyNumber_Solution(self, index):
        """
        使用三个指针分别指向 2 3 5
        """
        if index == 0:
            return 0
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while len(ugly) < index:
            n2, n3, n5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            minimal = min(n2, n3, n5)
            ugly.append(minimal)
            if minimal == n2:
                i2 += 1
            if minimal == n3:
                i3 += 1
            if minimal == n5:
                i5 += 1
        return ugly[-1]


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        index = 2
        r = self.s.GetUglyNumber_Solution(index)
        self.assertEqual(2, r)

    def test_2(self):
        index = 7
        r = self.s.GetUglyNumber_Solution(index)
        self.assertEqual(8, r)
