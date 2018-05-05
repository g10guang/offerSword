# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-05 13:34
# 题目描述：https://www.nowcoder.com/practice/445c44d982d04483b04a54f298796288?tpId=13&tqId=11213&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import sys

if sys.version_info < (3, 0):
    from Queue import Queue
else:
    from queue import Queue


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        result = []
        if pRoot is None:
            return result
        control = True
        queue = {True: Queue(), False: Queue()}
        queue[control].put(pRoot)
        while not queue[control].empty():
            t = []
            while not queue[control].empty():
                n = queue[control].get()
                t.append(n.val)
                if n.left:
                    queue[not control].put(n.left)
                if n.right:
                    queue[not control].put(n.right)
            control = not control
            result.append(t)
        return result
