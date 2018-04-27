# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-27 11:51
# 题目描述：https://www.nowcoder.com/practice/8ee967e43c2c4ec193b040ea7fbb10b8?tpId=13&tqId=11164&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    def NumberOf1(self, n):
        """
        解决方法
        根据牛客网系统，n 应该是 32 位 int 类型
        """
        return sum(1 for x in range(32) if n & (1 << x))

    def NumberOf2(self, n):
        """
        解决方案二
        """
        b = bin(n)
        if n >= 0:
            return sum(1 for x in b[2:] if x == '1')
        # 负数需要特殊处理
        b = b[3:]
        # 将 n 的绝对值，也就是正数各位取反后放入到 t
        t = [0] * 32
        i = 31
        # 首先填写高位
        for x in range(32-len(b)):
            t[i] = 1
            i -= 1
        for x in b:
            t[i] = 1 - int(x)
            i -= 1
        # 执行地位 +1 操作
        for i, x in enumerate(t):
            if x == 1:
                t[i] = 0
            else:
                t[i] = 1
                break
        # 计算 1 的个数
        return sum(1 for x in t if x == 1)


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def logic(self, n):
        return self.s.NumberOf1(n)

    def test_1(self):
        n = 1
        r = self.logic(n)
        self.assertEqual(r, 1)

    def test_2(self):
        n = 2
        r = self.logic(n)
        self.assertEqual(r, 1)

    def test_3(self):
        n = 3
        r = self.logic(n)
        self.assertEqual(r, 2)

    def test_4(self):
        n = -1
        r = self.logic(n)
        self.assertEqual(r, 32)
