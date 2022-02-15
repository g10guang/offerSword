package main

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param head ListNode类
 * @return int整型一维数组
 */
// https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035?tpId=13&tqId=11156&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
func printListFromTailToHead(head *ListNode) []int {
	result := make([]int, 0, 16)
	var fn func(node *ListNode)
	fn = func(node *ListNode) {
		if node == nil {
			return
		}
		fn(node.Next)
		result = append(result, node.Val)
	}
	fn(head)
	return result
}
