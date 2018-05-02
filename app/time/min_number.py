# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-02 09:27
# 题目描述：https://www.nowcoder.com/practice/8fecd3f8ba334add803bf2a06af1b993?tpId=13&tqId=11185&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def PrintMinNumber(self, numbers):
        """
        排序
        """
        s = self.sort(numbers)
        return ''.join(s)

    def sort(self, numbers):
        """
        使用插入1排序
        """
        s = list(map(lambda x: str(x), numbers))
        index = 1
        while index < len(s):
            k = index
            while k > 0 and self.compare2(s[k - 1], s[k]):
                s[k], s[k - 1] = s[k - 1], s[k]
                k -= 1
            index += 1
        return s

    def compare(self, s, t):
        """
        比较两个字符串的大小
        '321' > '3'
        """
        long, short = (s, t) if len(s) >= len(t) else (t, s)
        short = short * (len(long) // len(short) + 1)
        return (long > short) if s is long else (short > long)

    def compare2(self, s, t):
        """
        比较 s+t 与 t+s 的大小
        """
        return s+t > t+s


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        numbers = [3, 32, 321]
        r = self.s.PrintMinNumber(numbers)
        self.assertEqual('321323', r)
