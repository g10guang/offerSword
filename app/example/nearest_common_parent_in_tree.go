package main

import "testing"

type TreeNode struct {
	Value int
	Left  *TreeNode
	Right *TreeNode
}

// 寻找二叉树中两个节点的最近公共祖先
func nearestCommonParentNode(root *TreeNode, a, b int) int {
	var findNodeFn func(node *TreeNode) (bool, bool, int)
	findNodeFn = func(node *TreeNode) (bool, bool, int) {
		if node == nil {
			return false, false, -1
		}

		leftA, leftB, lv := findNodeFn(node.Left)
		if leftA && leftB {
			return true, true, lv
		}

		rightA, rightB, rv := findNodeFn(node.Right)
		if rightA && rightB {
			return true, true, rv
		}

		if leftA && rightB || leftB && rightA {
			return true, true, node.Value
		}

		findA := node.Value == a || leftA || rightA
		findB := node.Value == b || leftB || rightB

		return findA, findB, node.Value
	}

	left, right, val := findNodeFn(root)
	if left && right {
		return val
	}

	return -1
}

func Test_nearestCommonParentNode(t *testing.T) {
	type args struct {
		root   *TreeNode
		a      int
		b      int
		expect int
	}

	root := &TreeNode{
		Value: 3,
		Left: &TreeNode{
			Value: 5,
			Left: &TreeNode{
				Value: 6,
				Left:  nil,
				Right: nil,
			},
			Right: &TreeNode{
				Value: 2,
				Left: &TreeNode{
					Value: 7,
					Left:  nil,
					Right: nil,
				},
				Right: &TreeNode{
					Value: 4,
					Left:  nil,
					Right: nil,
				},
			},
		},
		Right: &TreeNode{
			Value: 1,
			Left: &TreeNode{
				Value: 0,
				Left:  nil,
				Right: nil,
			},
			Right: &TreeNode{
				Value: 8,
				Left:  nil,
				Right: nil,
			},
		},
	}

	cases := []args{
		{
			root:   root,
			a:      1,
			b:      5,
			expect: 3,
		},

		{
			root:   root,
			a:      6,
			b:      8,
			expect: 3,
		},

		{
			root:   root,
			a:      4,
			b:      5,
			expect: 5,
		},

		{
			root:   root,
			a:      4,
			b:      0,
			expect: 3,
		},
	}

	for _, c := range cases {
		real := nearestCommonParentNode(c.root, c.a, c.b)
		t.Logf("a=%d b=%d expect=%d real=%d", c.a, c.b, c.expect, real)
	}
}
