function solution(bridge_length, weight, truck_weights) {
  var answer = 0;

  const queue = [];
  let bridgeWeight = 0;
  for (let i = 0; i < bridge_length; i++) {
    queue.push(0);
  }

  while (queue.length !== 0) {
    answer += 1;
    bridgeWeight -= queue.shift();

    if (truck_weights.length !== 0) {
      if (bridgeWeight + truck_weights[0] <= weight) {
        let truck = truck_weights.shift();
        queue.push(truck);
        bridgeWeight += truck;
      } else {
        queue.push(0);
      }
    }
  }

  return answer;
}

console.log(solution(2, 10, [7, 4, 5, 6]));
