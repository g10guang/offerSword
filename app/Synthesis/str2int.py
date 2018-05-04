# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-04 13:16
# 题目描述：https://www.nowcoder.com/practice/1277c681251b4372bdef344468e4f26e?tpId=13&tqId=11202&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def StrToInt(self, s):
        if not s:
            return 0
        end = 0
        if s.startswith(('+', '-')):
            end = 1
        t, exp = 0, 1
        for i in range(len(s) - 1, end - 1, -1):
            if not s[i].isdigit():
                return 0
            t += (ord(s[i]) - ord('0')) * exp
            exp *= 10
        if s[0] == '-':
            t = -t
        return t


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        r = self.s.StrToInt('100')
        self.assertEqual(100, r)

    def test_2(self):
        r = self.s.StrToInt('12345')
        self.assertEqual(12345, r)

    def test_3(self):
        r = self.s.StrToInt('-1234')
        self.assertEqual(-1234, r)

    def test_4(self):
        r = self.s.StrToInt('-123+')
        self.assertEqual(0, r)

    def test_5(self):
        r = self.s.StrToInt('')
        self.assertEqual(0, r)
