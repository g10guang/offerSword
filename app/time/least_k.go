package main

import "container/heap"

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param input int整型一维数组
 * @param k int整型
 * @return int整型一维数组
 */
// https://www.nowcoder.com/practice/6a296eb82cf844ca8539b57c23e6e9bf?tpId=13&tqId=11182&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
func GetLeastNumbers_Solution(input []int, k int) []int {
	h := &intHeap{}
	for _, v := range input {
		heap.Push(h, v)
		if h.Len() > k {
			heap.Pop(h)
		}
	}
	return h.container
}

type intHeap struct {
	container []int
}

func (h *intHeap) Push(x interface{}) {
	v := x.(int)
	h.container = append(h.container, v)
}

func (h *intHeap) Pop() interface{} {
	l := h.Len()
	v := h.container[l-1]
	h.container = h.container[:l-1]
	return v
}

func (h *intHeap) Less(i, j int) bool {
	return h.container[i] > h.container[j]
}

func (h *intHeap) Len() int {
	return len(h.container)
}

func (h *intHeap) Swap(i, j int) {
	h.container[i], h.container[j] = h.container[j], h.container[i]
}
