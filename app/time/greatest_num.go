package main

/**
 *
 * @param array int整型一维数组
 * @return int整型
 */
func FindGreatestSumOfSubArray(array []int) int {
    // 动态规划
    if len(array) == 0 {
        return 0
    }

    lastDp := array[0]
    m := lastDp
    for i := 1; i < len(array); i++ {
        v := array[i]
        currentDp := max(lastDp+v, v)

        if currentDp > m {
            m = currentDp
        }

        lastDp = currentDp
    }

    return m
}

func max(a, b int) int {
    if a > b {
        return a 
    }

    return b
}


func FindGreatestSumOfSubArray2(array []int) int {
    // 贪心算法
    if len(array) == 0 {
        return 0
    }

	max := array[0]
    acc := max
    for _, v := range array[1:] {
        if sum := acc + v; sum > 0 {
            acc = sum
        } else {
            acc = v
        }

        if v > acc {
            acc = v
        }

        if acc > max {
            max = acc
        }
    }
    

    return max
}
