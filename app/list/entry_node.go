package main

// https://www.nowcoder.com/practice/253d2c59ec3e4bc68da16833f79a38e4?tpId=13&tqId=11208&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
// 解法：fast一次移动两个节点，slow一次移动一个节点。
// 起点A，成环点B，fast与slow相遇点C，BC+CB是还的长度
// 会得出公示：(AB + a * (BC + CB) + BC) * 2 = AB + b(BC + CB) + BC
// 最后推导得出：AB = (b - a) * (BC + CB) - BC
// 相当于p指针从head出发，q从C出发，p、q相遇时将会在B节点，也就是成环点
func EntryNodeOfLoop(pHead *ListNode) *ListNode {
	fast, slow := pHead, pHead
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
		if fast == slow {
			break
		}
	}
	if fast == nil || fast.Next == nil {
		return nil
	}
	fast = pHead
	for fast != slow {
		fast = fast.Next
		slow = slow.Next
	}
	return fast
}
