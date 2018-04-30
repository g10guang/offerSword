/*
 * @Author: wuyiqing 
 * @Date: 2018-04-29 17:36:30 
 * @Last Modified by: wuyiqing
 * @Last Modified time: 2018-04-29 17:42:43
 * 题目描述：https://www.nowcoder.com/practice/8a19cbe657394eeaac2f6ea9b0f6fcf6?tpId=13&tqId=11157&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
 */

/**
 * 思路：主要利用了递归的思想。
 * 根据中序遍历和先序遍历的结果，首先获得根节点，再获取左子树和右子树。
 * 左子树和右子树又可以根据对应的中序遍历和先序遍历获得。
 */

 function TreeNode(x) {
  this.val = x;
  this.left = null;
  this.right = null;
}

function reConstructBinaryTree(pre, vin) {
  // pre 和 vin 的长度一致
  if (pre.length > 1) {
    let root = new TreeNode(pre[0]);
    // 划分中序遍历数组
    let i = vin.indexOf(pre[0]);
    let leftVin = vin.slice(0, i);
    let rightVin = vin.slice(i + 1);
    // 获取先序遍历数组
    pre.shift();
    let leftPre = pre.slice(0, leftVin.length);
    let rightPre = pre.slice(leftPre.length, pre.length);
    root.left = reConstructBinaryTree(leftPre, leftVin);
    root.right = reConstructBinaryTree(rightPre, rightVin);
    return root;
  } else if (pre.length === 1) {
    return new TreeNode(pre[0]);
  }
}
