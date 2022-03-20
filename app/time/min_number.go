package main

import (
	"sort"
	"strconv"
	"strings"
)

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param numbers int整型一维数组
 * @return string字符串
 */
func PrintMinNumber(numbers []int) string {
	if len(numbers) == 0 {
		return ""
	}
	strs := make([]string, len(numbers))
	for i, v := range numbers {
		strs[i] = strconv.Itoa(v)
	}
	sort.Slice(strs, func(i, j int) bool {
		x := strs[i]
		y := strs[j]
		var idx int
		for idx = 0; idx < len(x) && idx < len(y); idx++ {
			if x[idx] > y[idx] {
				return false
			} else if x[idx] < y[idx] {
				return true
			}
		}
		// 具体哪个小，拼起来比较一下，思路比较清晰
		return x+y < y+x
	})
	notZeroIdx := -1
	for i, str := range strs {
		if str != "0" {
			notZeroIdx = i
			break
		}
	}
	// if notZeroIdx == -1 {
	// 	return "0"
	// }
	if notZeroIdx != 0 {
		strs[0], strs[notZeroIdx] = strs[notZeroIdx], strs[0]
	}
	return strings.Join(strs, "")
}
