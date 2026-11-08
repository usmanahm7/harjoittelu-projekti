"use strict";
const numbers = [];

while (true) {
  const num = parseInt(prompt("Anna luku:"));
  if (numbers.includes(num)) {
    alert("Luku on jo annettu!");
    break;
  }
  numbers.push(num);
}
numbers.sort((a, b) => a - b);

for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}