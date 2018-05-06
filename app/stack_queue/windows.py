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


class Solution2:
    """
    使用双端开口的队列实现
    """

    def maxInWindows(self, num, size):
        q = CircleQueue(size)
        ret = []
        if len(num) < size or size < 1:
            return ret
        for i in range(size - 1):
            # 将元素的下标而不是元素值加入到队列中
            while q.len() > 0 and num[q.tailElem()] <= num[i]:
                q.removeTailElem()
            q.enqueue(i)
        for i in range(size - 1, len(num)):
            x = num[i]
            while q.len() > 0 and num[q.tailElem()] <= x:
                q.removeTailElem()
            q.enqueue(i)
            ret.append(max(num[q.frontElem()], x))
            if i - q.frontElem() >= size - 1:
                q.deque()
        return ret


class CircleQueue:
    """
    底层使用数组实现的循环队列
    队列双端开头，既可以从队头去元素，也可以从队尾取元素
    """

    def __init__(self, size):
        self.size = size + 1
        self.maxLen = self.size - 1
        self.q = [None] * self.size
        self.front, self.tail = 0, 0

    def enqueue(self, x):
        if self.len() == self.maxLen:
            raise FullQueue
        self.q[self.tail] = x
        self.tail = (self.tail + 1) % self.size

    def deque(self):
        if self.len() == 0:
            raise EmptyQueue
        x = self.q[self.front]
        self.q[self.front] = None
        self.front = (self.front + 1) % self.size
        return x

    def len(self):
        return (self.tail - self.front + self.size) % self.size

    def frontElem(self):
        if self.len() == 0:
            raise EmptyQueue
        return self.q[self.front]

    def tailElem(self):
        if self.len() == 0:
            raise EmptyQueue
        return self.q[self.tail - 1]

    def removeTailElem(self):
        """
        移除队尾元素
        :return:
        """
        if self.len() == 0:
            raise EmptyQueue
        x = self.q[self.tail - 1]
        self.tail = (self.tail - 1) % self.size
        self.q[self.tail] = None
        return x


class FullQueue(Exception):
    pass


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution2()

    def test_1(self):
        nums = [2, 3, 4, 2, 6, 2, 5, 1]
        size = 3
        r = self.s.maxInWindows(nums, size)
        self.assertEqual([4, 4, 6, 6, 6, 5], r)

    def test_2(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        size = 3
        r = self.s.maxInWindows(nums, size)
        self.assertEqual([3, 3, 5, 5, 6, 7], r)
