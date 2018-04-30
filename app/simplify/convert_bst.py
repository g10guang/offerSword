# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-29 15:09
# 题目描述：https://www.nowcoder.com/practice/947f6eb80d944a84850b0538bf0ec3a5?tpId=13&tqId=11179&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        # 记录上一次访问的结点，上一次访问的结点为 None
        self.pre = None

    def Convert(self, pRootOfTree):
        """
        BST的中序遍历顺序就是从小到大的排序
        """
        self.inOrder(pRootOfTree)
        # 寻找第一个结点作为返回值
        if pRootOfTree:
            while pRootOfTree.left:
                pRootOfTree = pRootOfTree.left
        return pRootOfTree

    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        node.left = self.pre
        if self.pre:
            self.pre.right = node
        self.pre = node
        self.inOrder(node.right)


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        root = TreeNode(8)
        root.left = TreeNode(5)
        root.right = TreeNode(10)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(6)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(11)
        r = self.s.Convert(root)
        print(r)
