function solution(number, k) {
  const stack = [];
  let count = 0;

  for (const num of number) {
    while (count < k && stack[stack.length - 1] < num) {
      stack.pop();
      count += 1;
    }
    stack.push(num);
  }
  console.log(stack);

  while (count < k) {
    stack.pop();
    count += 1;
  }

  console.log(stack.join(""));

  return stack.join("");
}

//console.log(solution("1924", 2));
console.log(solution("4177252841"), 4);
