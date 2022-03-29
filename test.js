function check(queen, row) {
  for (let i = 0; i < row; i += 1) {
    if (
      queen[i] === queen[row] ||
      Math.abs(queen[i] - queen[row]) === row - i
    ) {
      return false; // 둘 수 없다면 false
    }
  }
  return true; // 모두 통과되면 true
}

function search(queen, row) {
  const n = queen.length;
  let count = 0;

  if (n === row) {
    // 체스판 끝에 도달했다면.. 재귀의 탈출 조건
    return 1;
  }

  for (let col = 0; col < n; col += 1) {
    queen[row] = col; // 우선 퀸을 둔다
    if (check(queen, row)) {
      // 퀸을 둘 수 있다면..
      count += search(queen, row + 1);
    }
  }
  return count;
}

function solution(n) {
  return search(Array(n).fill(0), 0);
}

console.log(solution(4));
