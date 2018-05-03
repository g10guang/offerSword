# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-03 12:15
# 题目描述：https://www.nowcoder.com/practice/3194a4f4cf814f63919d0790578d51f3?tpId=13&tqId=11197&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


import re


class Solution:
    def ReverseSentence(self, s):
        """
        使用正则表达式找出字母
        """
        if s.isspace():
            return s
        p = re.compile(r'(\w+[.!?]*)\s*')
        r = p.findall(s)
        return ' '.join(reversed(r))


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        s = 'student. a am I'
        r = self.s.ReverseSentence(s)
        self.assertEqual('I am a student.', r)

    def test_2(self):
        s = ' '
        r = self.s.ReverseSentence(s)
        self.assertEqual(' ', r)

    def test_3(self):
        s = 'Hello World!'
        r = self.s.ReverseSentence(s)
        self.assertEqual('World! Hello', r)

