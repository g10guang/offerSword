package main

// type ListNode struct {
// 	Val  int
// 	Next *ListNode
// }

/**
 *
 * @param pHead ListNode类
 * @return ListNode类
 */
// https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca?tpId=13&tqId=11168&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func ReverseList(pHead *ListNode) *ListNode {
	if pHead == nil {
		return nil
	}
	if pHead.Next == nil {
		return pHead
	}
	p := pHead
	q := pHead.Next
	for q != nil {
		t := q.Next
		q.Next = p
		p = q
		q = t
	}
	pHead.Next = nil
	return p
}
