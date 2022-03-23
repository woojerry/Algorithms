// 03/23
// 스택

function solution(s) {
  let answer = true;

  stack = [];
  for (let i of s) {
    if (i === "(") {
      stack.push(i);
    } else {
      if (stack.length === 0) {
        answer = false;
        break;
      } else {
        stack.pop();
      }
    }
  }
  if (stack.length !== 0) {
    answer = false;
  }
  return answer;
}
