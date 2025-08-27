package main

import "fmt"

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 *
 * @param num int整型一维数组
 * @param size int整型
 * @return int整型一维数组
 */
func maxInWindows(num []int, size int) []int {
    if len(num) == 0 || size <= 0 {
        return nil
    }
    if size == 1 {
        return num
    }

	var queueIdx []int
	var ret []int

	for i := 0; i < len(num); i++ {
		if len(queueIdx) == 0 {
			queueIdx = append(queueIdx, i)
			continue
		}

		// 向后收缩
		dropLeftIdx := -1
		for j, q := range queueIdx {
			if i-q+1 > size || num[q] <= num[i] {
				dropLeftIdx = j
			} else {
				break
			}
		}
		// 向前收缩
        dropRightIdx := len(queueIdx)
        for j := len(queueIdx)-1; j >= 0 && j > dropLeftIdx; j-- {
            if num[queueIdx[j]] <= num[i] {
                dropRightIdx = j
            } else {
                break
            }
        }
        fmt.Printf("[maxInWindows] i=%d num=%d dropLeftIdx=%d queueIdx=%v\n", 
            i, num[i], dropLeftIdx, queueIdx)
		queueIdx = queueIdx[dropLeftIdx+1:dropRightIdx]
		queueIdx = append(queueIdx, i)

		if i+1 >= size {
			ret = append(ret, num[queueIdx[0]])
		}
	}

	return ret
}
