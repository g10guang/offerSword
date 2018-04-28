# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-28 21:01
# 题目描述：https://www.nowcoder.com/practice/a861533d45854474ac791d90e447bafd?tpId=13&tqId=11176&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    def VerifySquenceOfBST(self, sequence):
        """
        思路：
        假设输入的 sequence = [3, 6, 5, 9, 11, 10, 8]，该输入为合法的输入
        最后一个元素为根结点，根据排序二叉树的特点，左自树所有结点都小于根结点，右子树所有结点都大于根结点（题目说明不存在重复元素）
        从 sequence 中分割中根结点和左右子树：
        root=8 left=[3, 6, 5] right=[9, 11, 10]
        如果 right 中存在 elem < root，则违反排序二叉树特性
        如果不违反，则递归判断 left 和 right 是否符合规则
        """
        if not sequence:
            return False
        return self.logic(sequence, 0, len(sequence)-1)

    def logic(self, sequence, start, end):
        if start >= end:
            return True
        root = sequence[end]
        for i in range(start, end):
            if sequence[i] > root:
                leftEnd = i - 1
                rightStart = i
                break
        else:
            leftEnd = end - 1
            rightStart = end
        for i in range(rightStart, end):
            if sequence[i] < root:
                return False
        return self.logic(sequence, start, leftEnd) and self.logic(sequence, rightStart, end-1)
