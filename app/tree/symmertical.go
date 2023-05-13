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
 * @return bool布尔型
 */
func isSymmetrical(pRoot *TreeNode) bool {
	if pRoot == nil {
		return true
	}

	var walkFn func(left, right *TreeNode) bool
	walkFn = func(left, right *TreeNode) bool {
		if left == nil {
			return right == nil
		}

		if right == nil {
			return false
		}

		if left.Val != right.Val {
			return false
		}

		if walkFn(left.Right, right.Left) {
			return walkFn(left.Left, right.Right)
		}

		return false
	}

	return walkFn(pRoot.Left, pRoot.Right)
}
