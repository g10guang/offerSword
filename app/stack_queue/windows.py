# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-05 18:46
# 题目描述：https://www.nowcoder.com/practice/1624bc35a45c42c0bc17d17fa0cba788?tpId=13&tqId=11217&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    """
    可以使用 O(1) 空间支持 Max 操作的栈
    使用两个栈可以实现一个队列
    因为窗口是从左到右滑动，其中的元素是先进先出的，符合队列的行为
    """

    def maxInWindows(self, num, size):
        queue = MaxQueue()
        ret = []
        if len(num) < size or size < 1:
            return ret
        for i in range(size - 1):
            queue.enqueue(num[i])
        for i in range(size - 1, len(num)):
            queue.enqueue(num[i])
            ret.append(queue.max())
            queue.dequeue()
        return ret


class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxElem = None

    def push(self, x):
        if self.stack:
            if x > self.maxElem:
                y = 2 * x - self.maxElem
                self.stack.append(y)
                self.maxElem = x
                # 经过上述操作，y > self.maxElem
            else:
                self.stack.append(x)
        else:
            self.stack.append(x)
            self.maxElem = x

    def pop(self):
        if not self.stack:
            raise EmptyStack
        y = self.stack.pop()
        if y > self.maxElem:
            ret = self.maxElem
            self.maxElem = 2 * self.maxElem - y
            return ret
        else:
            return y

    def top(self):
        if not self.stack:
            raise EmptyStack
        y = self.stack[-1]
        if y > self.maxElem:
            return self.maxElem
        else:
            return y

    def max(self):
        if not self.stack:
            raise EmptyStack
        return self.maxElem

    def isEmpty(self):
        return len(self.stack) == 0


class MaxQueue:
    """
    使用两个支持 max 操作的栈实现队列
    """

    def __init__(self):
        self.write = MaxStack()
        self.read = MaxStack()

    def enqueue(self, x):
        self.write.push(x)

    def dequeue(self):
        if self.read.isEmpty():
            while not self.write.isEmpty():
                t = self.write.pop()
                self.read.push(t)
        if self.read.isEmpty():
            raise EmptyQueue
        return self.read.pop()

    def max(self):
        try:
            writeMax = self.write.max()
        except EmptyStack:
            writeMax = None
        try:
            readMax = self.read.max()
        except EmptyStack:
            readMax = None
        if not writeMax and not readMax:
            raise EmptyQueue
        if writeMax and readMax:
            return max(writeMax, readMax)
        return writeMax or readMax


class EmptyStack(Exception):
    pass


class EmptyQueue(Exception):
    pass


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        nums = [2, 3, 4, 2, 6, 2, 5, 1]
        size = 3
        r = self.s.maxInWindows(nums, size)
        self.assertEqual([4, 4, 6, 6, 6, 5], r)
