package main

type listNode struct {
	val  int
	next *listNode
}

// 单向链表，每k个节点组成一组做翻转
func reverse(root *listNode, k int) *listNode {
	if root == nil || k <= 0 {
		return root
	}

	// (1->2)->(3->4)->5   ==> 2->1->4->3->5
	// (1->2->3)->(4->5) 	==> 3->2->1->5->4
	// (3->2->1)  (5->4)
	// 1.先分组 2.反转每一个小组 3.重新串联

	var parts []*listNode
	p := root
	for p != nil {
		parts = append(parts, p)
		for cnt := 0; cnt < k && p != nil; cnt++ {
			p = p.next
			// 清空尾部
			if cnt == k-1 {
				q := p.next
				p.next = nil
				p = q
			}
		}
	}

	var newParts []*listNode
	for _, part := range parts {
		newParts = append(newParts, reverseGroup(part))
	}

	return join(newParts)
}

func join(parts []*listNode) *listNode {
	if len(parts) == 0 {
		return nil
	}

	var lastTail *listNode
	for _, part := range parts {
		p := part
		if lastTail != nil {
			lastTail.next = p
		}

		for p != nil && p.next != nil {
			p = p.next
		}
		lastTail = p
	}

	return parts[0]
}

func reverseGroup(root *listNode) *listNode {
	var stack []int
	p := root
	for p != nil {
		stack = append(stack, p.val)
	}

	if len(stack) == 0 {
		return nil
	}

	var newRoot *listNode
	q := &listNode{
		val: stack[len(stack)-1],
	}
	newRoot = q
	stack = stack[:len(stack)-1]
	for len(stack) > 0 {
		last := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		n := &listNode{
			val: last,
		}
		q.next = n
		q = n
	}

	return newRoot
}
