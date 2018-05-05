# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-05 12:38
# 题目描述：https://www.nowcoder.com/practice/9023a0c988684a53960365b889ceaf5e?tpId=13&tqId=11210&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        """
        思路：
        1) if pNode.right is not None:
            pNode.right 的最左孩子 or pNode
        2) if pNode.right is None:
            i) pNode.next.left is pNode:
                左孩子，直接返回 pNode
            ii) pNode.next.right is pNode:
                右孩子，需要一直
            return pNode.next
        """
        if pNode is None:
            return None
        if pNode.right:
            n = pNode.right
            while n and n.left:
                n = n.left
            return n
        if pNode.next and pNode.next.left is pNode:
            return pNode.next
        n = pNode
        while n:
            if n.next and n.next.left is n:
                n = n.next
                break
            n = n.next
        return n


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.root = TreeLinkNode(8)
        # 左子树
        self.root.left = TreeLinkNode(6)
        self.root.left.next = self.root
        self.root.left.left = TreeLinkNode(5)
        self.root.left.right = TreeLinkNode(7)
        self.root.left.left.next = self.root.left
        self.root.left.right.next = self.root.left
        # 右子树
        self.root.right = TreeLinkNode(10)
        self.root.right.next = self.root
        self.root.right.left = TreeLinkNode(9)
        self.root.right.right = TreeLinkNode(11)
        self.root.right.left.next = self.root.right
        self.root.right.right.next = self.root.right
        
    def test_1(self):
        r = self.s.GetNext(self.root.left.left)
        self.assertTrue(8, r.val)

    def test_2(self):
        r = self.s.GetNext(self.root.right.right)
        self.assertTrue(r is None)

    def test_3(self):
        r = self.s.GetNext(self.root)
        self.assertEqual(9, r.val)

    def test_4(self):
        r = self.s.GetNext(self.root.left.left)
        self.assertEqual(6, r.val)
