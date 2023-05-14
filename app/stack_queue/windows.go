package main

/**
 *
 * @param num int整型一维数组
 * @param size int整型
 * @return int整型一维数组
 */
func maxInWindows(nums []int, size int) []int {
	// https://www.nowcoder.com/share/jump/14730551684072631718
	var result []int
	if len(nums) == 0 || len(nums) < size || size <= 0 {
		return result
	}

	var queue []int
	// init
	for idx := 0; idx < size-1; idx++ {
		val := nums[idx]

		// drop smaller than current val
		dropIdx := len(queue) - 1
		for dropIdx >= 0 && nums[queue[dropIdx]] < val {
			dropIdx--
		}
		queue = queue[:dropIdx+1]
		queue = append(queue, idx)
	}

	// process
	for start := 0; start+size-1 < len(nums); start++ {
		end := start + size - 1
		val := nums[end]
		{
			// drop old index
			dropIdx := 0
			for dropIdx < len(queue) && queue[dropIdx] < start {
				dropIdx++
			}
			queue = queue[dropIdx:]
		}

		{
			// drop smaller than current val
			dropIdx := len(queue) - 1
			for dropIdx >= 0 && nums[queue[dropIdx]] < val {
				dropIdx--
			}
			queue = queue[:dropIdx+1]
		}

		queue = append(queue, end)

		result = append(result, nums[queue[0]])
	}

	return result
}
