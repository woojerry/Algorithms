const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

let inputs = [];
let result = "";
let i = 0;
let sumZero = false;

while (!sumZero) {
  inputs.push(input[i].split(" "));
  let sum = Number(inputs[i][0]) + Number(inputs[i][1]);
  if (sum === 0) {
    sumZero = true;
  } else {
    result += sum.toString() + "\n";
  }
  i++;
}
console.log(result);
