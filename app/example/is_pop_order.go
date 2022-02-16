package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param pushV int整型一维数组
 * @param popV int整型一维数组
 * @return bool布尔型
 */
// https://www.nowcoder.com/practice/d77d11405cc7470d82554cb392585106?tpId=13&tqId=11174&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func IsPopOrder(pushV []int, popV []int) bool {
	lenPush := len(pushV)
	lenPop := len(popV)
	if lenPush != lenPop {
		return false
	}
	if lenPush == 0 {
		return true
	}
	var stack []int
	pushIdx, popIdx := 0, 0
	for pushIdx < lenPush && popIdx < lenPop {
		if len(stack) == 0 {
			stack = append(stack, pushV[pushIdx])
			pushIdx++
			continue
		}
		if stack[len(stack)-1] == popV[popIdx] {
			stack = stack[:len(stack)-1]
			popIdx++
			continue
		}
		stack = append(stack, pushV[pushIdx])
		pushIdx++
	}
	if pushIdx != lenPush {
		return false
	}
	if len(stack) != lenPop-popIdx {
		return false
	}
	for idx := len(stack) - 1; idx >= 0; idx-- {
		if stack[idx] != popV[popIdx] {
			return false
		}
		popIdx++
	}
	return true
}
