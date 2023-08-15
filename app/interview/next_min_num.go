package main

import "sort"

// minNum 给定一个自然数n和自然数数组nums（每个元素取值[0,9]），求由nums中元素组成的、小于n的最大数。
// 示例：n=23121，nums={2,4,9}，返回=22999
func minNum(nums []int, n int) int {
	if n <= 0 || len(nums) == 0 {
		return -1
	}

	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})

	// parts 从小到大
	var parts []int
	for v := n; v > 0; v = v / 10 {
		d := v % 10
		parts = append(parts, d)
	}

	if len(parts) == 1 && parts[0] <= nums[0] {
		return -1
	}

	var result []int
	var flag bool
	// 寻找替换的 idx 和值
	for idx := len(parts) - 1; idx >= 0; idx-- {
		if flag {
			// 这里替换为 minMax，后续都用 max(nums) 填充即刻
			result = append(result, nums[len(nums)-1])
			continue
		}

		v := parts[idx]
		minMax := -1
		for _, a := range nums {
			if a > v {
				break
			}

			minMax = a
		}

		result = append(result, minMax)
		flag = minMax < v && minMax != -1
	}

	if !flag {
		// 3456 [7,8,9] --> 999
		// 123 [1,2,3] --> 33
		// 321 [1,2,3] --> 313
		// 一直都用的当前值，需要退位
		var done bool
		for idx := len(result) - 1; idx >= 0; idx-- {
			v := result[idx]
			minMax := -1
			for _, a := range nums {
				// 寻找下一个更小的值
				if a >= v {
					break
				}

				minMax = a
			}

			if minMax == -1 {
				continue
			}

			// 找到了，将这位替换，然后其他都替换为最大值
			result[idx] = minMax
			for j := len(result) - 1; j > idx; j-- {
				result[j] = nums[len(nums)-1]
			}
			done = true
			break
		}

		if !done {
			// 减少一位，其他都用最大值
			result = result[1:]
			for i := range result {
				result[i] = nums[len(nums)-1]
			}
		}
	}

	var res int
	for _, v := range result {
		if v == -1 {
			v = nums[len(nums)-1]
		}
		res = res*10 + v
	}

	return res
}
