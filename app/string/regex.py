# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-04 15:05
# 题目描述：https://www.nowcoder.com/practice/45327ae22b7b413ea21df13ee7d6429c?tpId=13&tqId=11205&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if not pattern and not s:
            return True
        if pattern and s:
            pi = 0
            c = pattern[0]
            if self.is_any(pattern, pi):
                si = 0
                r = self.match(s, pattern[2:])
                while not r and si < len(s) and self.is_match(s[si], c):
                    r = self.match(s[si+1:], pattern[2:])
                    si += 1
                return r
            elif self.is_match(s[0], c):
                return self.match(s[1:], pattern[1:])
        return len(pattern) == 2 and pattern[-1] == '*'

    def is_any(self, pattern, pi):
        return pi + 1 < len(pattern) and pattern[pi + 1] == '*'

    def is_match(self, sc, pc):
        return pc == '.' or pc == sc


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        s = 'aaa'
        pattern = 'a.a'
        r = self.s.match(s, pattern)
        self.assertTrue(r)

    def test_2(self):
        s = 'aaa'
        pattern = 'ab*ac*a'
        r = self.s.match(s, pattern)
        self.assertTrue(r)

    def test_3(self):
        s = 'aaa'
        pattern = 'abdc'
        r = self.s.match(s, pattern)
        self.assertFalse(r)

    def test_4(self):
        s = 'hello'
        pattern = '.*'
        r = self.s.match(s, pattern)
        self.assertTrue(r)

    def test_5(self):
        s = ''
        pattern = '.*'
        r = self.s.match(s, pattern)
        self.assertTrue(r)

    def test_6(self):
        s = ''
        pattern = '.'
        r = self.s.match(s, pattern)
        self.assertFalse(r)
