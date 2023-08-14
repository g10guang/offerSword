package main

import (
	"sort"
	"strconv"
)

// nextNum 寻找下一个更大的数字
// 比如数字：1234， 输出 1243
// 比如 1243，则输出 1324
func nextNum(n int) int {
	str := strconv.Itoa(int(n))
	parts := make([]int, len(str))
	for i, s := range str {
		parts[i] = int(s - '0')
	}

	minIdx := len(parts) - 1
	rightMin := parts[minIdx]

	for idx := len(parts) - 2; idx >= 0; idx-- {
		n := parts[idx]
		if n >= rightMin {
			continue
		}

		parts[idx], parts[minIdx] = parts[minIdx], parts[idx]
		sub := parts[idx+1:]
		sort.Slice(sub, func(i, j int) bool {
			return sub[i] < sub[j]
		})
		break
	}

	var ret int
	for _, v := range parts {
		ret = ret*10 + v
	}

	return ret
}
