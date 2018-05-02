# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-02 10:39
# 题目描述：https://www.nowcoder.com/practice/1c82e8cf713b4bbeb2a5b31cf5b0417c?tpId=13&tqId=11187&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def FirstNotRepeatingChar(self, s):
        """
        由于所有字符都是字母，记录每个字符出现的次数，以及其出现的下标
        """
        if not s:
            return -1
        cnt = [0] * 256
        for c in s:
            cnt[ord(c)] += 1
        for i, c in enumerate(s):
            if cnt[ord(c)] == 1:
                return i


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        s = 'google'
        r = self.s.FirstNotRepeatingChar(s)
        self.assertEqual(4, r)

    def test_2(self):
        s = ''
        r = self.s.FirstNotRepeatingChar(s)
        self.assertEqual(-1, r)

    def test_3(self):
        s = 'a'
        r = self.s.FirstNotRepeatingChar(s)
        self.assertEqual(0, r)
