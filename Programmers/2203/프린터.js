function solution(priorities, location) {
  let answer = 0;

  queue = [];

  for (let i = 0; i < priorities.length; i++) {
    queue.push({ priority: priorities[i], index: i });
  }

  let count = 0;
  while (true) {
    let { priority, index } = queue.shift();

    const max = Math.max.apply(
      Math,
      queue.map((q) => q.priority)
    );

    if (priority >= max) {
      count++;
      if (index === location) {
        answer = count;
        break;
      }
    } else {
      queue.push({ priority: priority, index: index });
    }
  }

  return answer;
}

//console.log(solution([2, 1, 3, 2], 2));
console.log(solution([1, 1, 9, 1, 1, 1], 0));
