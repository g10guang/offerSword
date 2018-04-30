/*
 * @Author: wuyiqing 
 * @Date: 2018-04-29 10:55:35 
 * @Last Modified by: wuyiqing
 * @Last Modified time: 2018-04-29 11:15:52
 * 题目描述：https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035?tpId=13&tqId=11156&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
 */

/*function ListNode(x){
    this.val = x;
    this.next = null;
}*/

function printListFromTailToHead(head) {
  // 使用栈存放结果
  const values = [];
  let node = head;
  while (node) {
    values.unshift(node.val);
    node = node.next;
  }
  return values;
}
