# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-04 16:34
# 题目描述：https://www.nowcoder.com/practice/00de97733b8e4f97a3fb5c680ee10720?tpId=13&tqId=11207&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    def __init__(self):
        self.stack = Node(None)
        self.appear = set()
        self.removed = set()

    # 返回对应char
    def FirstAppearingOnce(self):
        return '#' if self.stack.next is None else self.stack.next.val

    def Insert(self, char):
        if char not in self.appear:
            self.appear.add(char)
            self.stack.push(char)
        else:
            if char not in self.removed:
                self.removed.add(char)
                self.stack.remove(char)

    def reset(self):
        self.stack = Node(None)
        self.appear = set()


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def push(self, x):
        p = self
        while p.next:
            p = p.next
        p.next = Node(x)

    def remove(self, x):
        p = self
        while p.next.val != x:
            p = p.next
        p.next = p.next.next


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.s.reset()
        self.s.Insert('g')
        self.s.Insert('o')
        self.s.Insert('o')
        self.s.Insert('g')
        self.s.Insert('l')
        self.s.Insert('e')
        self.assertEqual('l', self.s.FirstAppearingOnce())

    def test_2(self):
        self.s.reset()
        self.s.Insert('h')
        self.s.Insert('e')
        self.s.Insert('l')
        self.s.Insert('l')
        self.s.Insert('o')
        self.s.Insert('w')
        self.s.Insert('o')
        self.s.Insert('r')
        self.s.Insert('l')
        self.s.Insert('d')
        self.assertEqual('h', self.s.FirstAppearingOnce())
