# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-29 14:31
# 题目描述：https://www.nowcoder.com/practice/f836b2c43afc4b35ad6adc41ec941dba?tpId=13&tqId=11178&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        """
        先遍历一遍链表，克隆 label 和 next 的信息，random 信息放到第二次遍历设置
        使用 dict 做一个映射，key: origin-node  value: new-node
        """
        newHead = None
        p, q = pHead, None
        map = {}
        while p:
            t = RandomListNode(p.label)
            if not newHead:
                newHead = t
            else:
                q.next = t
            # 保存映射关系
            map[p] = t
            p = p.next
            q = t
        p = pHead
        q = newHead
        while p:
            if p.random:
                q.random = map[p.random]
            p = p.next
            q = q.next
        return newHead
