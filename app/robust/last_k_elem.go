package main

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 *
 * @param pListHead ListNode类
 * @param k int整型
 * @return ListNode类
 */
//  https://www.nowcoder.com/practice/529d3ae5a407492994ad2a246518148a?tpId=13&tqId=11167&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func FindKthToTail(pListHead *ListNode, k int) *ListNode {
	if k == 0 {
		return nil
	}
	fast := pListHead
	for i := 0; i < k; i++ {
		if fast == nil {
			return nil
		}
		if fast.Next == nil {
			if i == k-1 {
				return pListHead
			}
			return nil
		}

		fast = fast.Next

	}
	if fast == nil {
		return nil
	}
	slow := pListHead
	for fast != nil {
		fast = fast.Next
		slow = slow.Next
	}
	return slow
}
