package main

// type TreeNode struct {
//   Val int
//   Left *TreeNode
//   Right *TreeNode
// }

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param root TreeNode类
 * @param expectNumber int整型
 * @return int整型二维数组
 */
// https://www.nowcoder.com/practice/b736e784e3e34731af99065031301bca?tpId=13&tqId=11177&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func FindPath(root *TreeNode, expectNumber int) [][]int {
	// 深度优先遍历二叉树
	var result [][]int
	var fn func(node *TreeNode, path []int, sum int)
	fn = func(node *TreeNode, path []int, sum int) {
		if node == nil {
			return
		}
		if node.Left == nil && node.Right == nil {
			if sum+node.Val == expectNumber {
				result = append(result, append(path, node.Val))
				return
			}
		}
		fn(node.Left, append(path, node.Val), sum+node.Val)
		fn(node.Right, append(path, node.Val), sum+node.Val)
	}
	fn(root, nil, 0)
	return result
}
