# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-05 13:09
# 题目描述：https://www.nowcoder.com/practice/91b69814117f4e8097390d107d2efbe0?tpId=13&tqId=11212&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        """
        使用两个栈存储树的打印
        """
        if pRoot is None:
            return []
        # True 从左往右打印
        # False 从右往做打印
        control = True
        stack = {True: [], False: []}
        result = []
        stack[control].append(pRoot)
        while stack[True] or stack[False]:
            if stack[control]:
                result.append(list(reversed([x.val for x in stack[control]])))
            while stack[control]:
                n = stack[control].pop()
                if control:
                    if n.left:
                        stack[not control].append(n.left)
                    if n.right:
                        stack[not control].append(n.right)
                else:
                    if n.right:
                        stack[not control].append(n.right)
                    if n.left:
                        stack[not control].append(n.left)
            control = not control
        return result


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

        r = self.s.Print(root)
        self.assertEqual([[8], [10, 6], [5, 7, 9, 11]], r)
