// 02/17
function solution(progresses, speeds) {
  var answer = [];

  const days = progresses.map((progress, idx) =>
    Math.ceil((100 - progress) / speeds[idx])
  );

  let count = 1;
  let max = days.shift();

  for (const day of days) {
    if (day <= max) {
      count += 1;
    } else {
      answer.push(count);
      count = 1;
      max = day;
    }
  }
  answer.push(count);

  return answer;
}

console.log(solution([93, 30, 55], [1, 30, 5]));
