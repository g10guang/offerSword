# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-02 13:51
# 题目描述：https://www.nowcoder.com/practice/8b3b95850edb4115918ecebdf1b4d222?tpId=13&tqId=11192&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot):
        return self.recursive(pRoot)[0]

    def recursive(self, root):
        """
           递归从叶子往上走时候判断每个结点的左右子树高度相差是否在 1 内
        """
        if not root:
            return True, 0
        leftBalanced, leftHeight = self.recursive(root.left)
        if not leftBalanced:
            return False, 0
        rightBalanced, rightHeight = self.recursive(root.right)
        if rightBalanced and -1 <= leftHeight - rightHeight <= 1:
            return True, max(leftHeight, rightHeight) + 1
        else:
            return False, 0
