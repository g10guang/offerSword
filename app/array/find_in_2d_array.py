# coding=utf-8
# author: Xiguang Liu<g10guang@gmail.com>
# 2018-04-21 18:06
# 题目描述：https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=11154&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

import unittest


class Solution:

    def Find(self, target, array):
        """
        思路：
        从右上角开始搜索
        if r < target:
            缩小矩形规模
        elif r > target:
            缩小矩形规模
        else:
            找到
        因为矩形的缩小过程中每次都只是抛弃了比 target 小或者大的数，从而使矩形的规模不断缩小
        那么只要 target 存在矩形中，肯定会被找到
        :param target:
        :param array:
        :return:
        """
        row, col = len(array), len(array[0])
        x, y = 0, col - 1
        while x < row and y >= 0:
            r = array[x][y]
            if r < target:
                x += 1
            elif r > target:
                y -= 1
            else:
                return True
        return False


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_1(self):
        target = 5
        array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
        r = self.s.Find(target, array)
        self.assertFalse(r)

    def test_2(self):
        target = 7
        array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
        r = self.s.Find(target, array)
        self.assertTrue(r)
