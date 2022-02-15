package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param pre int整型一维数组
 * @param vin int整型一维数组
 * @return TreeNode类
 */
// https://www.nowcoder.com/practice/8a19cbe657394eeaac2f6ea9b0f6fcf6?tpId=13&tqId=11157&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func reConstructBinaryTree(pre []int, vin []int) *TreeNode {
	if len(vin) == 0 {
		return nil
	}
	rootVal := pre[0]
	root := &TreeNode{
		Val: rootVal,
	}
	rootIdx := -1
	for i, v := range vin {
		if v == rootVal {
			rootIdx = i
		}
	}
	if rootIdx == -1 {
		return nil
	}
	root.Left = reConstructBinaryTree(pre[1:], vin[:rootIdx])
	root.Right = reConstructBinaryTree(pre[rootIdx+1:], vin[rootIdx+1:])
	return root
}
