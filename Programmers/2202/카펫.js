function solution(brown, yellow) {
  var answer = [];

  const total = brown + yellow;
  for (let x = 1; x <= total; x++) {
    if (total % x === 0) {
      let y = total / x;
      if (x >= y) {
        if (2 * x + 2 * y - 4 === brown) {
          answer = [x, y];
        }
      }
    }
  }

  return answer;
}
