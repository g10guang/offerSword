package main

/**
 *
 * @param data int整型一维数组
 * @param k int整型
 * @return int整型
 */
//  https://www.nowcoder.com/practice/70610bf967994b22bb1c26f9ae901fa2?tpId=13&tqId=11190&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
func GetNumberOfK( nums []int ,  k int ) int {
    length := len(nums)
    start := 0
    end := length-1
    for start <= end {
        mid := (start+end)/2
        if nums[mid] == k {
            return GetNumberOfK(nums[mid+1:end+1], k) + GetNumberOfK(nums[start:mid], k) + 1
        } else if nums[mid] > k {
            end = mid - 1
        } else {
            start = mid + 1
        }
    }

    return 0
}
