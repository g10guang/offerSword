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
        如果链表环比较长会导致该算法的空间利用率比较底下
        """
        visited = set()
        p = pHead
        while p and p not in visited:
            visited.add(p)
            p = p.next
        return p


class Solution2:
    def EntryNodeOfLoop(self, pHead):
        """
        思路：
        1) 使用双指针追及方法先找到环中的一个结点 x
        2) 顺着环走计算环的长度 l
        3) p, q = pHead, pHead
            i) p 先走 l 步
            ii) p q 同步走
            当 p == q 时，p 所指向的结点就是入口结点
        """
        if pHead.next is None:
            return None
        p, q = pHead.next, pHead
        while p and q and p != q:
            p = p.next
            if p.next:
                p = p.next.next
            else:
                return None
            q = q.next
        if not p or not q:
            return None
        p = p.next
        l = 1
        while p != q:
            l += 1
            p = p.next
        p, q = pHead, pHead
        for _ in range(l):
            p = p.next
        while p != q:
            p = p.next
            q = q.next
        return p
