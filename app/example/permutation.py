# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-30 10:37
# 问题描述：https://www.nowcoder.com/practice/fe6b651b66ae47d7acce78ffdd9a96c7?tpId=13&tqId=11180&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:

    def __init__(self):
        self.result = []
        self.source = None
        self.visited = {}
        self.tmp = []

    def Permutation(self, ss):
        """
        回溯法
        """
        if not ss:
            return self.result
        self.source = sorted(ss)
        for i in range(len(self.source)):
            self.visited[i] = False
        self.logic()
        return self.result

    def logic(self):
        if len(self.tmp) == len(self.source):
            self.result.append(''.join(self.tmp))
            return
        for i, c in enumerate(self.source):
            if i > 0 and self.source[i-1] == self.source[i] and self.visited[i-1] is False:
                continue
            if self.visited[i] is False:
                self.tmp.append(c)
                self.visited[i] = True
                self.logic()
                self.visited[i] = False
                self.tmp.pop()


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        ss = ""
        r = self.s.Permutation(ss)
        self.assertEqual(r, [])

    def test_2(self):
        ss = "ab"
        r = self.s.Permutation(ss)
        self.assertEqual(['ab', 'ba'], r)

    def test_3(self):
        ss = "aa"
        r = self.s.Permutation(ss)
        self.assertEqual(['aa'], r)

    def test_4(self):
        ss = "aab"
        r = self.s.Permutation(ss)
        self.assertEqual(['aab', 'aba', 'baa'], r)
