# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-27 17:16
# 题目描述：https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca?tpId=13&tqId=11168&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None:
            return None
        t = pHead.next
        # 改为链表尾部
        pHead.next = None
        n = self.reverse(pHead, t)
        if n:
            return n
        else:
            return pHead

    def reverse(self, last, cur):
        if cur is None:
            return last
        t = cur.next
        cur.next = last
        return self.reverse(cur, t)
