function solution(numbers) {
  let answer = "";

  newNumbers = [];
  numbers.forEach((num) => {
    let newNum = String(num);
    for (let i = 0; i < 2; i++) {
      newNum += String(num);
    }
    newNumbers.push([newNum, num]);
  });

  newNumbers.sort().reverse();
  console.log(newNumbers);

  for (const [_, num] of newNumbers) {
    answer += num;
  }

  if (numbers.reduce((sum, curr) => sum + curr) === 0) {
    answer = "0";
  }
  return answer;
}

//console.log(solution([6, 10, 2]));
console.log(solution([3, 30, 34, 5, 9]));
