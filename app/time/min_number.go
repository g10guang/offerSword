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
    strs := make([]string, len(numbers))
    for i, v := range numbers {
        s := strconv.Itoa(v)
        strs[i] = s
    }

    sort.Slice(strs, func(i, j int) bool {
        x := strs[i]
        y := strs[j]
        return x + y < y + x
    })

    return strings.Join(strs, "")
}

func PrintMinNumber2(numbers []int) string {
	parseTenFn := func(n int) []int {
		var t []int
		// 转化为十进制
		for n > 0 {
			v := n % 10
			t = append(t, v)
			n = n / 10
		}
		// 翻转
		for i := 0; i < len(t)/2; i++ {
			t[i], t[len(t)-i-1] = t[len(t)-i-1], t[i]
		}

		return t
	}

	var compareFn func(at, bt []int) bool

	compareFn = func(at, bt []int) bool {
		for i := 0; i < len(at) && i < len(bt); i++ {
			if at[i] < bt[i] {
				return true
			} else if at[i] > bt[i] {
				return false
			}
		}

        if len(at) == len(bt) {
            return true // 一样大小，顺序不重要
        }

		// 大家前缀都是一样，那么对比的是 bt 后半截和 at
		longer := at
		shorter := bt
        if len(at) < len(bt) {
            longer = bt 
            shorter = at 
        }
		longer = longer[len(shorter):]

		res := compareFn(shorter, longer)
		if res { // 短的更小
			if len(at) < len(bt) {
				return true
			}
			return false
		}
		if len(at) > len(bt) { // 长的更小
			return true
		}
		return false
	}

	// 排序
	sort.Slice(numbers, func(i, j int) bool {
		at := parseTenFn(numbers[i])
		bt := parseTenFn(numbers[j])

		return compareFn(at, bt)
	})

	// 拼接字符串
	var res string
	for _, n := range numbers {
		s := strconv.Itoa(n)
		res += s
	}

    fmt.Printf("numbers=%v res=%v\n", numbers, res)

	return res
}
