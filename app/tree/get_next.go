package main

type TreeLinkNode struct {
	Val   int
	Left  *TreeLinkNode
	Right *TreeLinkNode
	Next  *TreeLinkNode
}

// GetNext https://www.nowcoder.com/share/jump/14730551683985846976
func GetNext(pNode *TreeLinkNode) *TreeLinkNode {
	if pNode == nil {
		return nil
	}

	if pNode.Right != nil {
		// must in right subtree's leftest node
		n := pNode.Right
		for n != nil && n.Left != nil {
			n = n.Left
		}

		return n
	}

	parent := pNode.Next
	if parent == nil {
		// pNode is the last node in tree
		return nil
	}

	if pNode == parent.Left {
		// next should scan parent
		return parent
	}

	n := parent
	for n.Next != nil {
		p := n.Next
		if p.Left == n {
			return p
		}

		n = n.Next
	}

	return nil
}

// 另外一种思路，先找到最顶端，然后再中序遍历二叉树
func GetNext2(pNode *TreeLinkNode) *TreeLinkNode {
	if pNode == nil {
		return nil
	}

	root := pNode
	for root.Next != nil {
		root = root.Next
	}

	var last *TreeLinkNode
	var walkFn func(n *TreeLinkNode) *TreeLinkNode
	walkFn = func(n *TreeLinkNode) *TreeLinkNode {
		if n.Left != nil {
			r := walkFn(n.Left)
			if r != nil {
				return r
			}
		}

		if last != nil && last == pNode {
			return n
		}

		last = n

		if n.Right != nil && n.Val <= pNode.Val {
			r := walkFn(n.Right)
			if r != nil {
				return r
			}
		}

		return nil
	}

	return walkFn(root)
}
