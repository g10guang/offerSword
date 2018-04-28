# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-28 18:11
# 题目描述：https://www.nowcoder.com/practice/9b4c81a02cd34f76be2659fa0d54342a?tpId=13&tqId=11172&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    def __init__(self):
        self.threshold = None
        self.matrix = None
        self.row = 0
        self.col = -1
        self.result = []
        self.resultLen = 0

    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        """
        思路：定义四个方向的走向 → ↓ ← ↑ 循环遍历，
        给每一个方向定义一个尽头然后更新方向的信息
        """
        self.threshold = {'right': len(matrix[0]) - 1, 'down': len(matrix) - 1, 'left': 0, 'up': 1}
        self.matrix = matrix
        self.resultLen = len(matrix) * len(matrix[0])
        while self.resultLen > len(self.result):
            self.right()
            self.down()
            self.left()
            self.up()
        return self.result

    def right(self):
        if self.resultLen == len(self.result):
            return
        while self.col < self.threshold['right']:
            self.col += 1
            self.result.append(self.matrix[self.row][self.col])
        self.threshold['right'] -= 1

    def down(self):
        if self.resultLen == len(self.result):
            return
        while self.row < self.threshold['down']:
            self.row += 1
            self.result.append(self.matrix[self.row][self.col])
        self.threshold['down'] -= 1

    def left(self):
        if self.resultLen == len(self.result):
            return
        while self.col > self.threshold['left']:
            self.col -= 1
            self.result.append(self.matrix[self.row][self.col])
        self.threshold['left'] += 1

    def up(self):
        if self.resultLen == len(self.result):
            return
        while self.row > self.threshold['up']:
            self.row -= 1
            self.result.append(self.matrix[self.row][self.col])
        self.threshold['up'] += 1


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        matrix = [[1]]
        expect = [1]
        r = self.s.printMatrix(matrix)
        self.assertEqual(r, expect)

    def test_2(self):
        matrix = [[1, 2], [3, 4]]
        expect = [1, 2, 4, 3]
        r = self.s.printMatrix(matrix)
        self.assertEqual(r, expect)

    def test_3(self):
        matrix = [[1], [2], [3], [4], [5]]
        expect = [1, 2, 3, 4, 5]
        r = self.s.printMatrix(matrix)
        self.assertEqual(r, expect)
