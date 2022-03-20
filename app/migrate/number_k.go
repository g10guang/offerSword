package main

/**
 *
 * @param data int整型一维数组
 * @param k int整型
 * @return int整型
 */
//  https://www.nowcoder.com/practice/70610bf967994b22bb1c26f9ae901fa2?tpId=13&tqId=11190&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
func GetNumberOfK(data []int, k int) int {
	low, high := 0, len(data)-1
	findIdx := -1
	for low <= high {
		mid := (low + high) / 2
		if data[mid] == k {
			findIdx = mid
			break
		}
		if data[mid] > k {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}
	if findIdx == -1 {
		return 0
	}

	lowCnt := 0
	for high := findIdx - 1; low <= high; {
		mid := (low + high) / 2
		if data[mid] == k {
			lowCnt = findIdx - mid
			high = mid - 1
		} else {
			low = mid + 1
		}
	}

	highCnt := 0
	for low := findIdx + 1; low <= high; {
		mid := (low + high) / 2
		if data[mid] == k {
			highCnt = mid - findIdx
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return lowCnt + highCnt + 1
}
