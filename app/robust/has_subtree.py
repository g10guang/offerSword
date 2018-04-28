# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-27 17:44
# 题目描述：https://www.nowcoder.com/practice/6e196c44c7004d15b1610b9afca8bd88?tpId=13&tqId=11170&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def HasSubtree(self, A, B):
        """
           用于防止 B 树一开始就是空
        """
        if B is None:
            return False
        return self.logic(A, B)

    def logic(self, A, B):
        if B is None:
            return True
        if A is None:
            return False
        r = False
        if A.val == B.val:
            r = self.logic(A.left, B.left) and self.logic(A.right, B.right)
        if not r:
            r = self.logic(A.left, B) or self.logic(A.right, B)
        return r


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        A = TreeNode(8)
        A.left = TreeNode(8)
        A.right = TreeNode(7)
        A.left.left = TreeNode(9)
        A.left.right = TreeNode(2)
        A.right.left = TreeNode(4)
        A.right.right = TreeNode(7)

        B = TreeNode(8)
        B.left = TreeNode(9)
        B.right = TreeNode(2)

        r = self.s.HasSubtree(A, B)

        self.assertTrue(r)
