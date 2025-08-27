package main

import (
	"container/heap"
	"fmt"
)

var bigHeap = &intHeap{
    max: true,
}
var smallHeap = &intHeap{
    max: false,
}

func Insert(num int){
    defer func() {
        fmt.Printf("[Insert] num=%d bigHeap=%v smallHeap=%v\n", num, bigHeap.data, smallHeap.data)
    }()
    rebalanceFn := func() {
        if smallHeap.Len() > bigHeap.Len() {
            // 预期 bigHeap 更长
            n := heap.Pop(smallHeap)
            heap.Push(bigHeap, n)
        }

        if bigHeap.Len() > smallHeap.Len() + 1 {
            n := heap.Pop(bigHeap)
            heap.Push(smallHeap, n)
        }

        if bigHeap.Len() > 0 && smallHeap.Len() > 0 && bigHeap.Top() > smallHeap.Top() {
            // 交换刚刚写入的元素
            v := heap.Pop(bigHeap)
            heap.Push(smallHeap, v)
            v = heap.Pop(smallHeap)
            heap.Push(bigHeap, v)
        }
    }

    defer rebalanceFn()
    if bigHeap.Len() == 0 {
        heap.Push(bigHeap, num)
        return 
    }

    if smallHeap.Len() == 0 {
        heap.Push(smallHeap, num)
        return 
    }

    st := smallHeap.Top()
    if num >= st {
        heap.Push(smallHeap, num)
    } else {
        heap.Push(smallHeap, num)
    }
}

func GetMedian() (m float64) {
    defer func() {
        fmt.Printf("[GetMedian] m=%v bigHeap=%v smallHeap=%v\n", m, bigHeap.data, smallHeap.data)
    }()
    
    if bigHeap.Len() == 0 {
        return float64(0)
    }

	if bigHeap.Len() == smallHeap.Len() {

        return ( float64(bigHeap.Top()) + float64(smallHeap.Top()) )  / 2
    }

    return float64(bigHeap.Top())
}

type intHeap struct {
    data []int 
    max bool 
}

func (h *intHeap) Less(i, j int) bool {
    if h.max {
        // 大顶堆，最大的放在头部，其他都比它小
        return h.data[i] > h.data[j]
    }

    // 小顶堆，最小的放在头部，其他都比它大
    return h.data[i] < h.data[j]
}

func (h *intHeap) Len() int {
    return len(h.data)
}

func (h *intHeap) Swap(i, j int) {
    h.data[i], h.data[j] = h.data[j], h.data[i]
}

func (h *intHeap) Push(x interface{}) {
    v := x.(int)
    h.data = append(h.data, v)
}

func (h *intHeap) Pop() interface{} {
    // pop 尾部
    v := h.data[len(h.data)-1]
    h.data = h.data[:len(h.data)-1]
    return v 
}

func (h *intHeap) Top() int {
    return h.data[0]
}
