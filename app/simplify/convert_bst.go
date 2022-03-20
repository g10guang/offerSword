package main

// import . "nc_tools"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/**
 *
 * @param pRootOfTree TreeNode类
 * @return TreeNode类
 */
//  https://www.nowcoder.com/practice/947f6eb80d944a84850b0538bf0ec3a5?tpId=13&tqId=11179&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func Convert(pRootOfTree *TreeNode) *TreeNode {
	if pRootOfTree == nil {
		return nil
	}
	order := make([]*TreeNode, 0, 1000)
	var traverse func(node *TreeNode)
	// 中序遍历，得出有序列表
	traverse = func(node *TreeNode) {
		if node == nil {
			return
		}
		traverse(node.Left)
		order = append(order, node)
		traverse(node.Right)
	}
	traverse(pRootOfTree)
	newRoot := order[0]
	newRoot.Left = nil
	for i := 0; i < len(order)-1; i++ {
		cur := order[i]
		next := order[i+1]
		cur.Right = next
		next.Left = cur
		next.Right = nil
	}
	return newRoot
}
