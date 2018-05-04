# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-03 15:55
# 题目描述：https://www.nowcoder.com/practice/7a0da8fc483247ff8800059e12d7caf1?tpId=13&tqId=11200&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def Sum_Solution(self, n):
        """
        借助 Python 的小 trick
        """
        return sum(range(1, n + 1))


class Solution2:
    """
    循环可以借助递归栈完成，那么问题就转移为如何判断递归是否应该结束
    """

    def __init__(self):
        self.result = 0

    def Sum_Solution(self, n):
        self.result += n
        # 借助布尔运算的逻辑短路判断递归结束
        n > 0 and self.Sum_Solution(n - 1)
        return self.result


class Solution3:
    def __init__(self):
        self.result = 0

    def Sum_Solution(self, n):
        """
        借助异常停止递归
        """
        try:
            t = 1 // n
        except ZeroDivisionError:
            return self.result
        self.result += n
        self.Sum_Solution(n - 1)
        return self.result


class Solution3:
    """
    使用字典映射函数
    """

    def __init__(self):
        self.result = 0
        self.index = 0
        self.map = {True: self.recursion, False: self.stop}

    def Sum_Solution(self, n):
        self.result = 0
        self.index = n
        self.map[self.index > 0]()
        return self.result

    def recursion(self):
        self.result += self.index
        self.index -= 1
        self.map[self.index > 0]()

    def stop(self):
        pass


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
       self.s = Solution3()

    def test_1(self):
        n = 1
        r = self.s.Sum_Solution(n)
        self.assertEqual(1, r)
