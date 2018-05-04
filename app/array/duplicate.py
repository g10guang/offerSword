# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-04 13:31
# 题目描述：https://www.nowcoder.com/practice/623a5ac0ea5b4e5f95552655361ae0a8?tpId=13&tqId=11203&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        """
        将每个元素映射到对应下标
        """
        index = 0
        while index < len(numbers):
            while numbers[index] != index:
                t = numbers[index]
                if numbers[t] == t:
                    duplication[0] = t
                    return True
                numbers[index] = numbers[t]
                numbers[t] = t
            index += 1
        return False


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        numbers = [2, 1, 3, 1, 4]
        duplucate = [0]
        r = self.s.duplicate(numbers, duplucate)
        self.assertEqual(True, r)
        self.assertEqual(1, duplucate[0])
