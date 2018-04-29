# coding=utf-8
# author: Xiguang Liu<g10guang@gmail.com>
# 2018-04-26 17:38
# 题目描述：https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035?tpId=13&tqId=11156&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

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
