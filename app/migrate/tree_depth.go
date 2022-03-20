package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param pRoot TreeNode类
 * @return int整型
 */
func TreeDepth(pRoot *TreeNode) int {
	var depthFn func(node *TreeNode) int
	depthFn = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		left := depthFn(node.Left)
		right := depthFn(node.Right)
		return max(left, right) + 1
	}
	return depthFn(pRoot)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
