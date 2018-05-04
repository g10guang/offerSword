# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-04 17:36
# 提米描述：https://www.nowcoder.com/practice/fc533c45b73a41b0b44ccba763f866ef?tpId=13&tqId=11209&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        p, q = pHead, None
        while p:
            while p.next and p.val == p.next.val:
                p = p.next
            if pHead.val == p.val:
                if pHead != p:
                    pHead = p.next
            else:
                if q.next != p:
                    q.next = p.next
                    p = p.next
                    continue
            q = p
            p = p.next
        return pHead


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(4)
        head.next.next.next.next.next = ListNode(4)
        head.next.next.next.next.next.next = ListNode(5)
        r = self.s.deleteDuplication(head)
        self.assertEqual(1, r.val)
        self.assertEqual(2, r.next.val)
        self.assertEqual(5, r.next.next.val)

    def test_2(self):
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(4)
        head.next.next.next.next.next = ListNode(4)
        head.next.next.next.next.next.next = ListNode(5)
        r = self.s.deleteDuplication(head)
        self.assertEqual(5, r.val)
        self.assertTrue(r.next is None)

    def test_3(self):
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(4)
        head.next.next.next.next.next = ListNode(4)
        head.next.next.next.next.next.next = ListNode(5)
        head.next.next.next.next.next.next.next = ListNode(5)
        r = self.s.deleteDuplication(head)
        self.assertTrue(r is None)
