package main

import (
	"strconv"
	"strings"
)

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
 * @param root TreeNode类
 * @return TreeNode类
 */
func Serialize(root *TreeNode) string {
	var parts []string
	var walkFn func(node *TreeNode)
	walkFn = func(node *TreeNode) {
		if node == nil {
			parts = append(parts, "#")
			return
		}

		parts = append(parts, strconv.Itoa(node.Val))
		walkFn(node.Left)
		walkFn(node.Right)
	}

	walkFn(root)
	return strings.Join(parts, ",")
}

func Deserialize(s string) *TreeNode {
	nodes := strings.Split(s, ",")

	offset := 0
	var parseSubTree func() *TreeNode
	parseSubTree = func() *TreeNode {
		if len(nodes) <= offset {
			return nil
		}

		strVal := nodes[offset]
		offset++
		if strVal == "#" {
			return nil
		}

		v, err := strconv.Atoi(strVal)
		if err != nil {
			return nil
		}

		node := &TreeNode{
			Val: v,
		}

		node.Left = parseSubTree()
		node.Right = parseSubTree()

		return node
	}

	root := parseSubTree()
	return root
}
