package main

import "fmt"

// 输入一个有序数组，输出该数组中平方后不一样的元素个数
func diffAbsNumInArray(arr []int) int {
	left := 0
	right := len(arr) - 1
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}

	var cnt int
	for left <= right {
		if left == right {
			cnt++
			break
		}
		lv := abs(arr[left])
		rv := abs(arr[right])

		if lv == rv {
			for left <= right {
				if abs(arr[left]) != rv {
					break
				}
				left++
			}

			for left <= right {
				if abs(arr[right]) != lv {
					break
				}
				right--
			}
		} else if lv > rv {
			left++
			cnt++
		} else {
			right--
			cnt++
		}
	}

	return cnt
}

func main() {
	type args struct {
		arr    []int
		expect int
	}

	cases := []args{
		{
			arr:    []int{-5, -2, -1, 0, -1, 2, 3, 4, 5},
			expect: 3,
		},
		{
			arr:    []int{-5, -2, -1, 0, 0, 0, -1, -1, 2, 3, 4, 5},
			expect: 2,
		},
	}

	for _, c := range cases {
		got := diffAbsNumInArray(c.arr)
		fmt.Printf("arr=%v expect=%d got=%d\n", c.arr, c.expect, got)
	}
}
