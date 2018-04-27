# coding=utf-8
# author: Xiguang Liu<g10guang@gmail.com>
# 2018-04-27 11:26
# 题目描述：https://www.nowcoder.com/practice/72a5a919508a4251859fb2cfb987a0e6?tpId=13&tqId=11163&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

import unittest


class Solution:
    def __init__(self):
        self.dp = {0: 0, 1: 1, 2: 2}

    def rectCover(self, number):
        """
        动态规划
        :param number:
        :return:
        """
        if number in self.dp:
            return self.dp[number]
        # 错误：f = self.rectCover(number-1) + self.rectCover(number-2)*2
        # 因为 self.rectCover(number-1) 已经包含了 self.rectCover(number-2) 的一种情况，这种情况值得琢磨
        f = self.rectCover(number-1) + self.rectCover(number-2)
        self.dp[number] = f
        return f


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        n = 3
        r = self.s.rectCover(n)
        self.assertEqual(r, 3)
