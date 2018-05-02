# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-02 12:59
# 题目描述：https://www.nowcoder.com/practice/6ab1d9a29e88450685099d45c9e31e46?tpId=13&tqId=11189&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        """
        思路：
        使用栈统计两个链表中的节点，每次 pop 一个，直到栈顶元素不相同
        """
        s1, s2 = [], []
        p = pHead1
        while p:
            s1.append(p)
            p = p.next
        q = pHead2
        while q:
            s2.append(q)
            q = q.next
        common = None
        while len(s1) > 0 and len(s2) > 0 and s1[-1] == s2[-1]:
            common = s1.pop()
            s2.pop()
        return common


class Solution2:
    def FindFirstCommonNode(self, pHead1, pHead2):
        """
        思路：
        1) 分别统计两个链表的长度，假设长度分别为：l1, l2
        2) 先让长的先走 long-short
        3） 使用两个指针共同前行，且一直判断是否存在公共结点
        """
        l1, l2 = 0, 0
        p, q = pHead1, pHead2
        while p:
            l1 += 1
            p = p.next
        while q:
            l2 += 1
            q = q.next
        p, q, long, short = (pHead1, pHead2, l1, l2) if l1 > l2 else (pHead2, pHead1, l2, l1)
        for _ in range(long - short):
            p = p.next
        while p and q and p != q:
            p = p.next
            q = q.next
        common = p if p and q else None
        return common
