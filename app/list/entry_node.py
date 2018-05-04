# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-04 17:01
# 题目描述：https://www.nowcoder.com/practice/253d2c59ec3e4bc68da16833f79a38e4?tpId=13&tqId=11208&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        """
        思路：
        将所有已经访问过的元素加入到集和中，如果访问到某个元素在集和中，那么该元素就是环的入口
        """
        visited = set()
        p = pHead
        while p and p not in visited:
            visited.add(p)
            p = p.next
        return p

