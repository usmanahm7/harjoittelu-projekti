"use strict";

const countStr = prompt("Montako kertaa noppaa heitetään?");
const count = parseInt(countStr);

let sum = 0;

for (let i = 0; i < count; i++) {
  const dice = Math.floor(Math.random() * 6) + 1;
  sum += dice;
}

document.querySelector("#target").innerHTML = `Silmälukujen summa on ${sum}.`;