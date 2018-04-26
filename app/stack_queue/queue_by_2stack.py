# coding=utf-8
# author: Xiguang Liu<g10guang@gmail.com>
# 2018-04-26 18:55
# 题目描述：https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6?tpId=13&tqId=11158&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    """
    使用两个栈实现一个队列
    以下的栈通过 list 实现
    """

    def __init__(self):
        self.writeStack = []
        self.readStack = []

    def push(self, node):
        """
        进栈写入到 writeStack 中
        :param node:
        :return:
        """
        self.writeStack.append(node)

    def pop(self):
        """
        如果 readStack 为空，那么从 writeStack 中导入内容
        从 readStack 中出栈
        :return:
        """
        if not self.readStack:
            # 这里不考虑 deepcopy
            self.readStack, self.writeStack = list(reversed(self.writeStack)), self.readStack
        return self.readStack.pop()
