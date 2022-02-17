const myMap = new Map();
myMap.set("a", 3);
myMap.set("c", 4);
myMap.set("b", 1);
myMap.set("d", 2);

console.log(myMap);
for (let i of myMap.values()) {
  console.log(i);
}
