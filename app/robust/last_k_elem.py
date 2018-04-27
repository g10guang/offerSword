# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-27 17:03
# 题目描述：https://www.nowcoder.com/practice/529d3ae5a407492994ad2a246518148a?tpId=13&tqId=11167&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        """
       使用双指针法，指针 p 和 q，q 比 p 先走 k 位，当 q 到达链表末尾时，p 指向的元素就是倒数第 k 个
        :param head:
        :param k:
        :return:
        """
        q, p = head, head
        for _ in range(k):
            if q is None:
                return None
            q = q.next
        while q is not None:
            q = q.next
            p = p.next
        return p
