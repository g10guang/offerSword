# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-28 19:10
# 题目描述：https://www.nowcoder.com/practice/4c776177d2c04c2494f2555c9fcc1e49?tpId=13&tqId=11173&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    """
    使用额外 O(1) 空间创建一个能够求出最小值的栈
    更加详细的算法说明可以参考：https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
    以下简单介绍算法：
    设当前栈中最小元素是 min

    Push 假设插入元素为 x
    if x >= min:
        push x into stack
    else:
        y = 2*x - min
        push y into stack

    Pop 假设栈顶元素为 y
    if y >= min:
        Pop y
        return y
    else:
        r = min
        min = x*min - y
        Pop y
        return r

    简单证明：
    假设把更小的元素 x 入栈：
    x < min
    ==> 2*x - min < x
    也就是栈顶元素为 y = 2*x-min 时候，y < min 必然成立。
    当 y = 2*x-min 成立时，证明最小元素将要被弹出，需要更新栈中最小元素:
    min = 2*min - y
    上述更新操作是于插入操作 y= 2*x-min 互为逆操作上述

    类似，可以使用额外 O(1) 空间构造一个支持 max 函数的栈
    """

    def __init__(self):
        self.stack = []
        self.minElem = None

    def push(self, node):
        if self.stack:
            if node >= self.minElem:
                self.stack.append(node)
            else:
                self.stack.append(2 * node - self.minElem)
                self.minElem = node
        else:
            # 当前栈为空
            self.stack.append(node)
            self.minElem = node

    def pop(self):
        if self.stack:
            y = self.stack.pop()
            if y >= self.minElem:
                return y
            else:
                x = self.minElem
                self.minElem = 2 * self.minElem - y
                return x
        else:
            return None

    def top(self):
        if self.stack:
            y = self.stack[-1]
            if y >= self.minElem:
                return y
            else:
                return self.minElem
        else:
            return None

    def min(self):
        if self.stack:
            return self.minElem
        else:
            return None

