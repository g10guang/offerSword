package main

import (
	"fmt"
	"sort"
	"testing"
)

// 给定一个自然数n和自然数数组nums（每个元素取值[0,9]），求由nums中元素组成的、小于n的最大数。 ​
// 示例：n=23121，nums={2,4,9}，返回=22999
func maxNumber(n int, elems []int) int {
	// 思路：从尾部开始填充，如果用了一个更小的数字，则头部可以尽量取大数

	genNpFn := func(num int) []int {
		var np []int
		for x := num; x > 0; x = x / 10 {
			d := x % 10
			np = append(np, d)
		}

		// 翻转
		for i := 0; i < len(np)/2; i++ {
			np[i], np[len(np)-i-1] = np[len(np)-i-1], np[i]
		}

		return np
	}

	np := genNpFn(n)
	fmt.Printf("np=%v\n", np)

	genNFn := func(arr []int) int {
		var res int
		for _, v := range arr {
			res = res*10 + v
		}
		return res
	}

	sort.Slice(elems, func(i, j int) bool {
		return elems[i] < elems[j]
	})

	genMaxFn := func(cnt int) int {
		var res int
		for i := 0; i < cnt; i++ {
			res = elems[len(elems)-1] + res*10
		}

		return res
	}

	// 保留不了高位
	if elems[0] > np[0] {
		return genMaxFn(len(np) - 1)
	}

	find := false
	for _, e := range elems {
		if e == np[0] {
			find = true
		}
	}

	if find {
		newN := genNFn(np[1:])
		// 递归处理
		sub := maxNumber(newN, elems)
		fmt.Printf("newN=%d sub=%d\n", newN, sub)
		// 如果位数是和newN一样的，则使用此回答，否则使用
		if len(genNpFn(newN)) == len(genNpFn(sub)) {
			// 找到答案
			ret := np[0]
			for i := 0; i < len(np)-1; i++ {
				ret *= 10
			}
			return ret + sub
		}
	}

	// 取仅小于最高位的方案
	var res int
	for _, e := range elems {
		if e < np[0] {
			res = e
		} else {
			break
		}
	}
	fmt.Printf("res1=%d\n", res)
	for i := 0; i < len(np)-1; i++ {
		res = res * 10
	}
	res = res + genMaxFn(len(np)-1)
	fmt.Printf("res2=%d\n", res)
	return res

}

func Test_maxNumber(t *testing.T) {
	type args struct {
		n      int
		elems  []int
		expect int
	}

	cases := []args{
		{
			n:      23121,
			elems:  []int{2, 4, 9},
			expect: 22999,
		},

		{
			n:      23121,
			elems:  []int{4, 8, 9},
			expect: 9999,
		},

		{
			n:      29129,
			elems:  []int{2, 8, 9},
			expect: 28999,
		},
	}

	for _, c := range cases {
		real := maxNumber(c.n, c.elems)
		t.Logf("n=%d elems=%v expect=%d real=%d", c.n, c.elems, c.expect, real)
	}
}
