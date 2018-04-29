# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-29 13:18
# 题目描述：https://www.nowcoder.com/practice/b736e784e3e34731af99065031301bca?tpId=13&tqId=11177&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        # 记录结果的二维链表
        self.result = []
        self.curPath = []
        self.curSum = 0

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        """
        因为结点的数值有可能为负数，所以必须遍历所有的叶子结点，也就是不能够提前判断当前你路径失败
        """
        if root is None:
            return self.result
        self.curPath.append(root.val)
        self.curSum += root.val
        # 判断是否是叶子结点，如果是叶子结点需要判断是否 curSum == expectNumber
        if root.left is None and root.right is None:
            if self.curSum == expectNumber:
                self.result.append(self.curPath[:])
        else:
            self.FindPath(root.left, expectNumber)
            self.FindPath(root.right, expectNumber)
        self.curSum -= root.val
        self.curPath.pop()
        return self.result
