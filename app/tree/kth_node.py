# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-05 16:45
# 题目描述：https://www.nowcoder.com/practice/ef068f602dde4d28aab2b210e859150a?tpId=13&tqId=11215&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    思路：
    中序遍历二叉搜索树的结果就是从小到大排列的结果
    """
    def __init__(self):
        self.index = 0
        self.result = None

    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if k <= 0:
            return None
        self.index = k
        self.inOrder(pRoot)
        return self.result

    def inOrder(self, node):
        if node:
            self.inOrder(node.left)
            self.index -= 1
            if self.index == 0:
                self.result = node
                return
            self.inOrder(node.right)

