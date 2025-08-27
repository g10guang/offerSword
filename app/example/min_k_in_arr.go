package main

import (
	"container/heap"
	"fmt"
)

type intHeap struct {
	data []int
}

func (h *intHeap) Len() int {
	return len(h.data)
}

func (h *intHeap) Swap(i, j int) {
	h.data[i], h.data[j] = h.data[j], h.data[i]
}

func (h *intHeap) Less(i, j int) bool {
	return h.data[i] > h.data[j]
}

func (h *intHeap) Push(x any) {
	h.data = append(h.data, x.(int))
}

func (h *intHeap) Top() int {
	return h.data[0]
}

func (h *intHeap) Pop() any {
	v := h.data[len(h.data)-1]
	h.data = h.data[:len(h.data)-1]
	return v
}
func minKinArr(arr []int, k int) []int {
	myHeap := &intHeap{}

	for _, v := range arr {
		if myHeap.Len() >= k {
			t := myHeap.Top()
			if t > v {
				heap.Pop(myHeap)
				heap.Push(myHeap, v)
			}
		} else {
			heap.Push(myHeap, v)
		}
	}

	return myHeap.data
}

func main() {
	type args struct {
		arr    []int
		k      int
		expect []int
	}
	cases := []args{
		{
			arr:    []int{4, 5, 1, 6, 2, 7, 3, 8},
			k:      4,
			expect: []int{1, 2, 3, 4},
		},

		{
			arr:    []int{0, 1, 2, 1, 2},
			k:      3,
			expect: []int{0, 1, 1},
		},
	}

	for _, c := range cases {
		got := minKinArr(c.arr, c.k)
		fmt.Printf("arr=%v k=%d expect=%v got=%v\n", c.arr, c.k, c.expect, got)
	}
}
