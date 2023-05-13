package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param pHead ListNode类
 * @return ListNode类
 */
func deleteDuplication(pHead *ListNode) *ListNode {
	p := pHead
    var last *ListNode
	for p != nil && p.Next != nil {
		q := p
		for q.Next != nil && q.Val == q.Next.Val {
			q = q.Next
		}
        
        if p == q {
            // no duplicate, move forward
            last = p
            p = p.Next
            continue
        }

        if last != nil {
            // delete duplicate
            last.Next = q.Next
            p = q.Next
            continue
        }
        
        // delete first node
        p = q.Next
        pHead = p
	}

	return pHead
}
