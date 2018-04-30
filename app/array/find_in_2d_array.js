/*
 * @Author: wuyiqing 
 * @Date: 2018-04-29 09:48:22 
 * @Last Modified by: wuyiqing
 * @Last Modified time: 2018-04-29 09:58:06
 * 题目描述：https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=11154&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
 */
const assert = require('assert');

/**
 * 思路：此题主要采用的是动态规划的思想，将二维数组一步一步缩小来寻找目标数。
 * 可以选择右上角（或左下角）的数 n 作为参考点，来缩小数组的规模。
 * 当一个数大于 n 时，说明目标数必定不在第一行，则可以删除第一行。
 * 当一个数小于 n 时，说明目标数必定不在最后一列，则可以删除最后一列。
 * 等于 n，则找到目标数，以此类推直到数组大小为 0。
 */
function Find(target, array) {
  // 不直接修改数组，使用两个变量来标志数组的大小
  let x = 0;
  let y = array[0].length - 1;
  
  while (x < array.length && y >= 0) {
    count++;
    if (target === array[x][y]) {
      return true;
    }

    if (target < array[x][y]) {
      y--;
    } else {
      x++;
    }
  }
  return false;
}

function testFind() {
  let array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]];
  assert.equal(Find(7, array), true);
  assert.equal(Find(5, array), false);
}

testFind();