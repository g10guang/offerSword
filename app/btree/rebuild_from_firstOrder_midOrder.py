# coding=utf-8
# author: Xiguang Liu<g10guang@gmail.com>
# 2018-04-26 17:54
# 题目描述：https://www.nowcoder.com/practice/8a19cbe657394eeaac2f6ea9b0f6fcf6?tpId=13&tqId=11157&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        """
        使用递归重构二叉树
        思路：
        1、找出根结点（先序遍历的第一个结点）
        2、找出属于左子树的先序优先遍历和左子树的中序遍历
        3、找出属于右子树的先序遍历和右子树的中序遍历
        从而将问题转化为规模更小的子问题，递归解决
        :param pre:
        :param tin:
        :return:
        """
        if pre:
            # 还有结点
            root = pre[0]
            rootIndex = 0
            for i, n in enumerate(tin):
                if n == root:
                    rootIndex = i
                    break
            tree = TreeNode(root)
            tree.left = self.reConstructBinaryTree(pre[1:rootIndex + 1], tin[:rootIndex])
            tree.right = self.reConstructBinaryTree(pre[rootIndex + 1:], tin[rootIndex + 1:])
            return tree
        return None
