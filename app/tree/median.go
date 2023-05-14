package main

import (
	"container/heap"
	"fmt"
)

type intHeap struct {
	maxHeap bool
	data    []int
}

func (h intHeap) Len() int {
	return len(h.data)
}

func (h intHeap) Less(i, j int) bool {
	if h.maxHeap {
		// max heap
		return h.data[i] > h.data[j]
	}
	// mix heap
	return h.data[i] < h.data[j]
}

func (h intHeap) Swap(i, j int) {
	h.data[i], h.data[j] = h.data[j], h.data[i]
}

func (h *intHeap) Push(x interface{}) {
	h.data = append(h.data, x.(int))
}

func (h *intHeap) Pop() interface{} {
	n := h.data[h.Len()-1]
	h.data = h.data[:h.Len()-1]
	return n
}

func (h intHeap) top() int {
	return h.data[0]
}

var maxHeap = &intHeap{maxHeap: true}
var minHeap = &intHeap{maxHeap: false}
var cnt int

func Insert(num int) {
	fmt.Printf("maxHeap=%v minHeap=%v cnt=%d num=%d median=%f\n",
		maxHeap.data, minHeap.data, cnt, num, GetMedian())
	cnt++
	// maxHeap maintain the small side nums
	// minHeap maintain the big side nums
	// insert into maxHeap first
	if maxHeap.Len() == 0 {
		heap.Push(maxHeap, num)
		return
	}

	maxTop := maxHeap.top()

	if num > maxTop {
		// insert into minHeap
		heap.Push(minHeap, num)
		// rebalance
		for minHeap.Len() > maxHeap.Len() {
			v := heap.Pop(minHeap)
			heap.Push(maxHeap, v)
		}
	} else {
		// insert into maxHeap
		heap.Push(maxHeap, num)
		for maxHeap.Len() > minHeap.Len() {
			v := heap.Pop(maxHeap)
			heap.Push(minHeap, v)
		}
	}
}

func GetMedian() float64 {
	if maxHeap.Len() == 0 && minHeap.Len() == 0 {
		return 0
	}

	if maxHeap.Len() > minHeap.Len() {
		return float64(maxHeap.top())
	}

	if minHeap.Len() > maxHeap.Len() {
		return float64(minHeap.top())
	}

	return float64(maxHeap.top()+minHeap.top()) / 2
}
