# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-05 12:59
# 题目描述：https://www.nowcoder.com/practice/ff05d44dfdb04e1d83bdbdab320efbcb?tpId=13&tqId=11211&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        return self.logic(pRoot.left, pRoot.right)

    def logic(self, s, t):
        if s and t:
            return s.val == t.val and self.logic(s.left, t.right) and self.logic(s.right, t.left)
        return s is None and t is None


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(2)
        self.root.left.left = TreeNode(3)
        self.root.right.right = TreeNode(3)
        self.root.left.right = TreeNode(4)
        self.root.right.left = TreeNode(4)

    def test_1(self):
        r = self.s.isSymmetrical(self.root)
        self.assertTrue(r)

    def test_2(self):
        r = self.s.isSymmetrical(None)
        self.assertTrue(r)

    def test_3(self):
        self.root.left.left.left = TreeNode(10)
        r = self.s.isSymmetrical(self.root)
        self.assertFalse(r)