"use strict";

const numbers = [];

while (true) {
  const num = parseInt(prompt("Anna luku (0 lopettaa):"));
  if (num === 0) {
    break;
  }
  numbers.push(num);
}

numbers.sort((a, b) => b - a);

for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}