function solution(tickets) {
  const answer = [];

  const map = new Map();

  for (const [st, ed] of tickets) {
    if (map.has(st)) {
      map.get(st).push(ed);
    } else {
      map.set(st, [ed]);
    }
  }

  for (const value of map.values()) {
    value.sort().reverse();
  }

  const stack = ["ICN"];
  while (stack.length !== 0) {
    let top = stack.pop();

    if (!map.has(top) || map.get(top).length === 0) {
      answer.push(top);
    } else {
      stack.push(top);
      stack.push(map.get(top).pop());
    }
  }

  return answer.reverse();
}

// console.log(
//   solution([
//     ["ICN", "JFK"],
//     ["HND", "IAD"],
//     ["JFK", "HND"],
//   ])
// );

console.log(
  solution([
    ["ICN", "SFO"],
    ["ICN", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "ICN"],
    ["ATL", "SFO"],
  ])
);
