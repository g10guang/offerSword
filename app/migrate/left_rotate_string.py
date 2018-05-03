# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-03 12:00
# 题目描述：https://www.nowcoder.com/practice/12d959b108cb42b1ab72cef4d36af5ec?tpId=13&tqId=11196&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    def LeftRotateString(self, s, n):
        """
        采用翻手算法：
        假设将 s="abcXYZdef" 循环左移 3 位可以分为以下三步：
        1) m="abc"  进行对称操作 ==> m="cba"
        2) n="XYZdef" 进行对称操作 ==> n="fedZYX"
        3) p=m+n="cbafedZYX" 进行对称操作 ==> p="XYZdefabc"
        """
        if not s:
            return s
        n %= len(s)
        m, r = list(s[:n]), list(s[n:])
        self.minor(m)
        self.minor(r)
        m.extend(r)
        self.minor(m)
        return ''.join(m)

    def minor(self, slist):
        """
        执行镜像操作
        """
        p, q = 0, len(slist) - 1
        while p < q:
            slist[p], slist[q] = slist[q], slist[p]
            p, q = p + 1, q - 1
        return slist


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        s = "abcXYZdef"
        n = 3 + len(s)
        r = self.s.LeftRotateString(s, n)
        self.assertEqual("XYZdefabc", r)

    def test_2(self):
        s = ""
        n = 0
        r = self.s.LeftRotateString(s, n)
        self.assertEqual('', r)

