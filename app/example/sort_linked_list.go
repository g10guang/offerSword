package main

import (
	"fmt"
	"testing"
)

type LinkListNode struct {
	Value int
	Next  *LinkListNode
}

func (n *LinkListNode) String() []int {
	var values []int
	for p := n; p != nil; p = p.Next {
		values = append(values, p.Value)
	}

	return values
}

func NewLinkListFromSlice(arr []int) *LinkListNode {
	var head *LinkListNode
	var last *LinkListNode
	for _, v := range arr {
		node := &LinkListNode{
			Value: v,
			Next:  nil,
		}

		if last != nil {
			last.Next = node
		}
		last = node
		if head == nil {
			head = node
		}
	}

	return head
}

// 给定一个链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表
func sortLinkList(head *LinkListNode) *LinkListNode {
	// 冒泡排序，将最大的沉到最后
	listLen := 0
	for p := head; p != nil; p = p.Next {
		listLen++
	}

	for i := 0; i < listLen; i++ {
		var last *LinkListNode
		p := head
		for j := 0; j < listLen-i; j++ {
			// 将最大值挪到最后
			if p != nil && p.Next != nil {
				fmt.Printf("list=%v i=%d j=%d p=%d pnext=%d\n", head.String(), i, j, p.Value, p.Next.Value)
				next := p.Next
				if p.Value > next.Value {
					// 比较大小做互换
					if last != nil {
						last.Next = next
					}
					last = next
					if head == p {
						head = next
					}
					p.Next = next.Next
					next.Next = p
					// p 不需要移动
				} else {
					// p 需要移动
					last = p
					p = p.Next
				}
			}
		}
	}

	return head
}

func Test_sortLinkList(t *testing.T) {
	type args struct {
		head   []int
		expect []int
	}

	cases := []args{
		{
			head:   []int{4, 2, 1, 3},
			expect: []int{1, 2, 3, 4},
		},

		{
			head:   []int{4, 3, 2, 1},
			expect: []int{1, 2, 3, 4},
		},

		{
			head: []int{-1,5,3,4,0},
			expect: []int{-1, 0, 3, 4, 5},
		},
	}

	for _, c := range cases {
		head := NewLinkListFromSlice(c.head)
		got := sortLinkList(head)
		t.Logf("head=%v headList=%v expect=%v got=%v", c.head, head.String(), c.expect, got.String())
	}
}
