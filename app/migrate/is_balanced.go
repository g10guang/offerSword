package main

// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

/**
 *
 * @param pRoot TreeNode类
 * @return bool布尔型
 */
// func IsBalancedSorted_Solution(pRoot *TreeNode) bool {
// 	var traverse func(node *TreeNode) (depth int, leftMax int, rightMin int, balanced bool)
// 	traverse = func(node *TreeNode) (depth int, min int, max int, balanced bool) {
// 		if node == nil {
// 			return 0, -1, -1, true
// 		}
// 		leftDepth, leftMin, leftMax, leftBalanced := traverse(node.Left)
// 		if !leftBalanced || (leftMax != -1 && node.Val < leftMax) {
// 			return 0, 0, 0, false
// 		}

// 		rightDepth, rightMin, rightMax, rightBalanced := traverse(node.Right)
// 		if !rightBalanced || (rightMin != -1 && node.Val > rightMin) {
// 			return 0, 0, 0, false
// 		}

// 		depthDiff := leftDepth - rightDepth
// 		if depthDiff > 1 || depthDiff < -1 {
// 			return 0, 0, 0, false
// 		}
// 		depth = leftDepth
// 		if depthDiff < 0 {
// 			depth = rightDepth
// 		}
// 		depth++
// 		min = node.Val
// 		if leftMin != -1 {
// 			min = leftMin
// 		}
// 		max = node.Val
// 		if rightMax != -1 {
// 			max = rightMax
// 		}
// 		return depth, min, max, true
// 	}

// 	_, _, _, balanced := traverse(pRoot)
// 	return balanced
// }

// https://www.nowcoder.com/practice/8b3b95850edb4115918ecebdf1b4d222?tpId=13&tqId=11192&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func IsBalanced_Solution(pRoot *TreeNode) bool {
	var traverse func(node *TreeNode) (depth int, balanced bool)
	traverse = func(node *TreeNode) (depth int, balanced bool) {
		if node == nil {
			return 0, true
		}
		leftDepth, leftBalanced := traverse(node.Left)
		if !leftBalanced {
			return 0, false
		}

		rightDepth, rightBalanced := traverse(node.Right)
		if !rightBalanced {
			return 0, false
		}

		depthDiff := leftDepth - rightDepth
		if depthDiff > 1 || depthDiff < -1 {
			return 0, false
		}
		depth = leftDepth
		if depthDiff < 0 {
			depth = rightDepth
		}
		depth++
		return depth, true
	}

	_, balanced := traverse(pRoot)
	return balanced
}
