# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-05 19:27
# 题目描述：https://www.nowcoder.com/practice/c61c6999eecb4b8f88a98f66b273a3cc?tpId=13&tqId=11218&tPage=4&rp=4&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.matrix = None
        self.path = None
        self.visited = None
        self.direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def hasPath(self, matrix, rows, cols, path):
        """
        matrix 传递的是一维数组，还要对其进行下标映射
        """
        self.row = rows
        self.col = cols
        self.matrix = matrix
        self.path = path
        self.visited = [False, ] * (self.row * self.col)
        for i in range(rows):
            for j in range(cols):
                if self.search(i, j, 0):
                    return True
        return False

    def search(self, x, y, pi):
        if pi == len(self.path):
            return True
        if 0 <= x < self.row and 0 <= y < self.col:
            if self.visited[x * self.col + y]:
                return False
            if self.elem(x, y) == self.path[pi]:
                self.visited[x * self.col + y] = True
                for m, n in self.direction:
                    if self.search(x + m, y + n, pi + 1):
                        return True
                self.visited[x * self.col + y] = False
        return False

    def elem(self, x, y):
        return self.matrix[x * self.col + y]


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        matrix = ['a', 'b', 'c', 'e', 's', 'f', 'c', 's', 'a', 'd', 'e', 'e']
        r = self.s.hasPath(matrix, 3, 4, 'bcced')
        self.assertTrue(r)
        r = self.s.hasPath(matrix, 3, 4, 'abcb')
        self.assertFalse(r)
