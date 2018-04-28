# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-28 20:34
# 题目描述：https://www.nowcoder.com/practice/7fe2212963db4790b57431d9ed259701?tpId=13&tqId=11175&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

import sys

# queue 在 Python2 和 Python3 中不一致
if sys.version_info > (3, 0):
    import queue as queue
else:
    import Queue as queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        """
        从上往下，从左到右遍历二叉树，广度有限遍历，使用一个辅助队列
        """
        result = []
        q = queue.Queue()
        if root is None:
            return result
        q.put(root)
        while not q.empty():
            t = q.get()
            result.append(t.val)
            if t.left:
                q.put(t.left)
            if t.right:
                q.put(t.right)
        return result
