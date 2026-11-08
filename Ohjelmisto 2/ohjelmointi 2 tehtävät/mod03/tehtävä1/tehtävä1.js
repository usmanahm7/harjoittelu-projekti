"use strict";

const numbers = [];

for (let i = 0; i < 5; i++) {
  const num = parseInt(prompt("Anna luku:"));
  numbers.push(num);
}

for (let i = numbers.length - 1; i >= 0; i--) {
  console.log(numbers[i]);
}