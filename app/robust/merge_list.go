package main

/*
 * type ListNode struct{
 *   Val int
 *   Next *ListNode
 * }
 */

/**
 *
 * @param pHead1 ListNode类
 * @param pHead2 ListNode类
 * @return ListNode类
 */
//  https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337?tpId=13&tqId=11169&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func Merge(pHead1 *ListNode, pHead2 *ListNode) *ListNode {
	if pHead1 == nil {
		return pHead2
	}
	if pHead2 == nil {
		return pHead1
	}
	p := pHead1
	q := pHead2
	var root, t *ListNode
	for p != nil && q != nil {
		var n *ListNode
		if p.Val < q.Val {
			n = p
			p = p.Next
		} else {
			n = q
			q = q.Next
		}
		n.Next = nil
		if root == nil {
			root = n
			t = n
		} else {
			t.Next = n
			t = n
		}
	}
	if p != nil {
		t.Next = p
	}
	if q != nil {
		t.Next = q
	}
	return root
}
