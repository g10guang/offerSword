# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-04 15:40
# 题目描述：https://www.nowcoder.com/practice/6f8c901d091949a5837e24bb82a731f2?tpId=13&tqId=11206&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


import re


class Solution2:
    def __init__(self):
        self.pattern = re.compile(r'^[\+\-]?\d*(\.\d+)?([eE][\+\-]?\d+)?$')

    def isNumeric(self, s):
        return self.pattern.match(s)


class Solution:
    def __init__(self):
        # 如果是以 0 开头，后面就不能够跟随其他数字
        self.unsigned_pattern = re.compile(r'^[1-9][0-9]*|^0+')

    # s字符串
    def isNumeric(self, s):
        """
        判断规则：
        (+|-)?(无符号整数)(.无符号整数)*(E|e[+-]?无符号整数)
        """
        # +.123 也是合法的
        if not s.startswith(('+.', '-.')):
            s = self.signed(s)
            if s is None:
                return False
            if s == '':
                return True
        else:
            s = s[1:]
        if s[0] == '.':
            s = self.unsigned(s[1:])
        if s is None:
            return False
        if s == '':
            return True
        if s[0] == 'E' or s[0] == 'e':
            s = self.signed(s[1:])
        if s is None:
            return False
        return s == ''

    def unsigned(self, s):
        """
        判断是否是无符号整数
        """
        r = self.unsigned_pattern.match(s)
        if r is None:
            return None
        return s[r.end():]

    def signed(self, s):
        """
        判断是否是有符号数
        """
        if s.startswith(('+', '-')):
            return self.unsigned(s[1:])
        return self.unsigned(s)


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution2()

    def test_1(self):
        s = '100'
        self.assertTrue(self.s.isNumeric(s))

    def test_2(self):
        s = '5e2'
        self.assertTrue(self.s.isNumeric(s))

    def test_3(self):
        s = '-123'
        self.assertTrue(self.s.isNumeric(s))

    def test_4(self):
        s = '3.1415926'
        self.assertTrue(self.s.isNumeric(s))

    def test_5(self):
        s = '-1e-16'
        self.assertTrue(self.s.isNumeric(s))

    def test_6(self):
        s = '12e'
        self.assertFalse(self.s.isNumeric(s))

    def test_7(self):
        s = '1a3.14'
        self.assertFalse(self.s.isNumeric(s))

    def test_8(self):
        s = '1.2.3'
        self.assertFalse(self.s.isNumeric(s))

    def test_9(self):
        s = '+5'
        self.assertTrue(self.s.isNumeric(s))

    def test_10(self):
        s = '+-5'
        self.assertFalse(self.s.isNumeric(s))

    def test_11(self):
        s = '12e+3.4'
        self.assertFalse(self.s.isNumeric(s))

    def test_12(self):
        s = '-.123'
        self.assertTrue(self.s.isNumeric(s))
