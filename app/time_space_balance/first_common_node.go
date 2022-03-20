package main

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 *
 * @param pHead1 ListNode类
 * @param pHead2 ListNode类
 * @return ListNode类
 */
func FindFirstCommonNode(pHead1 *ListNode, pHead2 *ListNode) *ListNode {
	listlen := func(node *ListNode) int {
		l := 0
		for node != nil {
			l++
			node = node.Next
		}
		return l
	}
	l1 := listlen(pHead1)
	l2 := listlen(pHead2)

	var long *ListNode
	var short *ListNode
	step := 0
	if l1 > l2 {
		long = pHead1
		short = pHead2
		step = l1 - l2
	} else {
		long = pHead2
		short = pHead1
		step = l2 - l1
	}

	for i := 0; i < step && long != nil; i++ {
		long = long.Next
	}

	for long != nil && short != nil && long != short {
		long = long.Next
		short = short.Next
	}
	return long
}
