package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param pRoot1 TreeNode类
 * @param pRoot2 TreeNode类
 * @return bool布尔型
 */
// https://www.nowcoder.com/practice/6e196c44c7004d15b1610b9afca8bd88?tpId=13&tqId=11170&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func HasSubtree(pRoot1 *TreeNode, pRoot2 *TreeNode) bool {
	if pRoot2 == nil {
		return false
	}
	if pRoot1 == nil {
		return false
	}
	if isMatchSubTree(pRoot1, pRoot2) {
		return true
	}
	return HasSubtree(pRoot1.Left, pRoot2) || HasSubtree(pRoot1.Right, pRoot2)
}

func isMatchSubTree(p, q *TreeNode) bool {
	if q == nil {
		return true
	}
	if p == nil {
		return false
	}
	if p.Val == q.Val {
		return isMatchSubTree(p.Left, q.Left) && isMatchSubTree(p.Right, q.Right)
	}
	return false
}
