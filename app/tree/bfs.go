package main

/*
 * type TreeNode struct {
 *   Val int
 *   Left *TreeNode
 *   Right *TreeNode
 * }
 */

/**
 *
 * @param pRoot TreeNode类
 * @return int整型二维数组
 */
func Print2(pRoot *TreeNode) [][]int {
	// https://www.nowcoder.com/share/jump/14730551684034623931
	var result [][]int
	var walkFn func(queue []*TreeNode)
	walkFn = func(queue []*TreeNode) {
		var line []int
		var next []*TreeNode
		for _, node := range queue {
			if node == nil {
				continue
			}

			line = append(line, node.Val)
			next = append(next, node.Left, node.Right)
		}

		if len(line) > 0 {
			result = append(result, line)
			walkFn(next)
		}

	}

	walkFn([]*TreeNode{pRoot})

	return result
}
