package main

// https://www.nowcoder.com/practice/4c776177d2c04c2494f2555c9fcc1e49?tpId=13&tqId=11173&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
var normalStack []int
var minimalStack []int

func Push(node int) {
	normalStack = append(normalStack, node)
	length := len(minimalStack)
	if length == 0 {
		minimalStack = append(minimalStack, node)
	} else {
		minVal := minimalStack[length-1]
		if minVal < node {
			minimalStack = append(minimalStack, minVal)
		} else {
			minimalStack = append(minimalStack, node)
		}
	}
}

func Pop() {
	length := len(normalStack)
	normalStack = normalStack[:length-1]
	minimalStack = minimalStack[:length-1]
}

func Top() int {
	length := len(normalStack)
	return normalStack[length-1]
}

func Min() int {
	length := len(normalStack)
	return minimalStack[length-1]
}
