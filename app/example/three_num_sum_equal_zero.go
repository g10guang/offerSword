package main

import (
	"fmt"
	"sort"
)

// 已知一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
func threeNumSumEqualZero(arr []int) [][]int {
	var result [][]int

	sort.Slice(arr, func(i, j int) bool {
		return arr[i] < arr[j]
	})

	for i := 0; i < len(arr)-2; i++ {
		if i > 0 && arr[i] == arr[i-1] {
			continue
		}

		// 寻找两数之和等于 -arr[i]
		target := -arr[i]
		left := i + 1
		right := len(arr) - 1
		for left < right {
			sum := arr[left] + arr[right]
			if target == sum {
				result = append(result, []int{arr[i], arr[left], arr[right]})
				left++
				right--
			} else if target > sum {
				left++
			} else {
				right--
			}
		}
	}

	return result
}

func main() {
	type args struct {
		arr    []int
		expect [][]int
	}

	cases := []args{
		{
			arr:    []int{-1, 0, 1, 2, -1, -4},
			expect: [][]int{{-1, -1, 2}, {1, 0, 1}},
		},
	}

	for _, c := range cases {
		got := threeNumSumEqualZero(c.arr)
		fmt.Printf("arr=%v expect=%v got=%v\n", c.arr, c.expect, got)
	}
}
