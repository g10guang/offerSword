# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-05 13:55
# 题目描述：https://www.nowcoder.com/practice/cf7e25aa97c04cc1a68c8f040e71fb84?tpId=13&tqId=11214&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    使用先序+中序遍历方法序列化二叉树
    """

    def Serialize(self, root):
        preVisited = []
        inVisited = []
        self.preOrder(root, preVisited)
        self.inOrder(root, inVisited)
        return preVisited, inVisited

    def preOrder(self, node, t):
        if node:
            t.append(node.val)
            self.preOrder(node.left, t)
            self.preOrder(node.right, t)

    def inOrder(self, node, t):
        if node:
            self.inOrder(node.left, t)
            t.append(node.val)
            self.inOrder(node.right, t)

    def Deserialize(self, s):
        preVisited, inVisited = s[0], s[1]
        if len(inVisited) == 0:
            return None
        root = TreeNode(preVisited[0])
        i = inVisited.index(preVisited[0])
        root.left = self.Deserialize((preVisited[1:i + 1], inVisited[:i]))
        root.right = self.Deserialize((preVisited[i + 1:], inVisited[i + 1:]))
        return root


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        root = TreeNode(8)
        # 左子树
        root.left = TreeNode(6)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(7)
        # 右子树
        root.right = TreeNode(10)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(11)

        pre, in_ = self.s.Serialize(root)

        r = self.s.Deserialize((pre, in_))

        self.assertEqual(r.val, 8)
        self.assertEqual(r.left.val, 6)
        self.assertEqual(r.left.left.val, 5)
        self.assertEqual(r.left.right.val, 7)
        self.assertEqual(r.right.val, 10)
        self.assertEqual(r.right.left.val, 9)
        self.assertEqual(r.right.right.val, 11)

