// 02/17
function solution(participant, completion) {
  var answer = "";

  const hashMap = new Map();

  for (const i of participant) {
    if (!hashMap.get(i)) {
      hashMap.set(i, 1);
    } else {
      hashMap.set(i, hashMap.get(i) + 1);
    }
  }

  for (const i of completion) {
    if (hashMap.get(i)) {
      hashMap.set(i, hashMap.get(i) - 1);
    }
  }

  for (const i of hashMap.keys()) {
    if (hashMap.get(i) > 0) {
      answer = i;
    }
  }

  return answer;
}

//solution(["leo", "kiki", "eden"], ["eden", "kiki"]);
console.log(
  solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
);
