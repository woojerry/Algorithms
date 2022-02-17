// 02/17
function solution(array, commands) {
  var answer = [];

  for (const command of commands) {
    const i = command[0];
    const j = command[1];
    const k = command[2];

    if (i === j) {
      answer.push(array[i - 1]);
    } else {
      const newArray = array.slice(i - 1, j);
      newArray.sort((a, b) => a - b);
      answer.push(newArray[k - 1]);
    }
  }

  return answer;
}

console.log(
  solution(
    [1, 5, 2, 6, 3, 7, 4],
    [
      [2, 5, 3],
      [4, 4, 1],
      [1, 7, 3],
    ]
  )
);
