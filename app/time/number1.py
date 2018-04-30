# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-30 14:44
# 题目描述：https://www.nowcoder.com/practice/bd7f978302044eee894445e244c7eee6?tpId=13&tqId=11184&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        """
        暴力破解
        """
        return sum(self.oneCount(x) for x in range(1, n + 1))

    def oneCount(self, k):
        cnt = 0
        while k:
            k, t = divmod(k, 10)
            if t == 1:
                cnt += 1
        return cnt


class Solution2:
    def __init__(self):
        self.cnt = 0
        self.curOneNum = 0
        self.nList = []
        self.n = 0

    def NumberOf1Between1AndN_Solution(self, n):
        """
        使用排列组合方法
        使用 [0..9] 10 个数组排列组合为不超过 n 的数字，且计算其中 1 的个数
        """
        self.n = n
        # 对 n 进行切割
        while n:
            n, k = divmod(n, 10)
            self.nList.append(k)
        self.logic(len(self.nList) - 1, True)
        return self.cnt

    def logic(self, index, threshold):
        if index < 0:
            self.cnt += self.curOneNum
            return
        for k in range(10):
            if threshold and k > self.nList[index]:
                return
            if k == 1:
                self.curOneNum += 1
            self.logic(index - 1, threshold=(threshold and k == self.nList[index]))
            if k == 1:
                self.curOneNum -= 1


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s2 = Solution2()
        self.s = Solution()

    def test_1(self):
        n = 1
        r = self.s2.NumberOf1Between1AndN_Solution(n)
        self.assertEqual(1, r)

    def test_2(self):
        n = 13
        r = self.s2.NumberOf1Between1AndN_Solution(n)
        self.assertEqual(6, r)

    def test_3(self):
        n = 10000
        r = self.s2.NumberOf1Between1AndN_Solution(n)
        self.assertEqual(4001, r)

    def test_4(self):
        n = 100
        expect = self.s.NumberOf1Between1AndN_Solution(n)
        print('=======')
        r = self.s2.NumberOf1Between1AndN_Solution(n)
        self.assertEqual(expect, r)
