# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-27 17:28
# 题目描述：https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337?tpId=13&tqId=11169&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead2 is None:
            return pHead1
        if pHead1 is None:
            return pHead2
        p, q = pHead1, pHead2
        newHead = None
        last = None
        while p is not None and q is not None:
            if p.val <= q.val:
                n = p
                p = p.next
            else:
                n = q
                q = q.next
            if newHead is None:
                newHead = n
                last = newHead
            else:
                last.next = n
                last = n
        r = p or q
        last.next = r
        return newHead
