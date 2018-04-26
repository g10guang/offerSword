# coding=utf-8
# author: Xiguang Liu<g10guang@gmail.com>
# 2018-04-26 17:38
# 题目描述：https://www.nowcoder.com/practice/4060ac7e3e404ad1a894ef3e17650423?tpId=13&tqId=11155&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        """
        递归输出
        :param listNode:
        :return:
        """
        if not hasattr(self, 'result'):
            self.result = []
        if listNode:
            self.printListFromTailToHead(listNode.next)
            self.result.append(listNode.val)

        return self.result
