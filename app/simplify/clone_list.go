package main

type RandomListNode struct {
	Label  int
	Next   *RandomListNode
	Random *RandomListNode
}

/**
 *
 * @param pHead RandomListNode类
 * @return RandomListNode类
 */
// https://www.nowcoder.com/practice/f836b2c43afc4b35ad6adc41ec941dba
func Clone(head *RandomListNode) *RandomListNode {
	if head == nil {
		return nil
	}
	root := &RandomListNode{
		Label: head.Label,
	}
	p := head
	q := root
	m := make(map[*RandomListNode]*RandomListNode)
	// 复制Next
	for p != nil {
		m[p] = q
		if p.Next != nil {
			q.Next = &RandomListNode{
				Label: p.Next.Label,
			}
			q = q.Next
			p = p.Next
		} else {
			break
		}
	}
	// 复制Random
	p = head
	q = root
	for ; p != nil; p, q = p.Next, q.Next {
		if p.Random == nil {
			continue
		}
		t := m[p.Random]
		q.Random = t
	}
	return root
}
