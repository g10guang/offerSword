package main

/*
 * type TreeNode struct {
 *   Val int
 *   Left *TreeNode
 *   Right *TreeNode
 * }
 */

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param pRoot TreeNode类
 * @return int整型二维数组
 */
func Print(pRoot *TreeNode) [][]int {
	var result [][]int
	if pRoot == nil {
		return result
	}

	var walkFn func(stack []*TreeNode, direction bool)
	walkFn = func(stack []*TreeNode, diretion bool) {
		if len(stack) == 0 {
			return
		}

		var next []*TreeNode
		var line []int
		for len(stack) > 0 {
			// pop node
			length := len(stack)
			node := stack[length-1]
			stack = stack[:length-1]

			if node == nil {
				continue
			}

			line = append(line, node.Val)
			if diretion {
				next = append(next, node.Right, node.Left)
			} else {
				next = append(next, node.Left, node.Right)
			}
		}

		if len(line) > 0 {
			result = append(result, line)
		}
		walkFn(next, !diretion)

		return
	}

	walkFn([]*TreeNode{pRoot}, false)

	return result
}
