package main

var stack1 []int
var stack2 []int

// https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6?tpId=13&tqId=11158&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func Push(node int) {
	stack1 = append(stack1, node)
}

func Pop() int {
	if len(stack2) == 0 {
		// stack2 空时，将stack1的内容倒到stack2中
		for len(stack1) > 0 {
			node := stack1[len(stack1)-1]
			stack1 = stack1[:len(stack1)-1]
			stack2 = append(stack2, node)
		}
	}
	l := len(stack2)
	node := stack2[l-1]
	stack2 = stack2[:l-1]
	return node
}
