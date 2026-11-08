"use strict";

const dogs = [];

for (let i = 0; i < 6; i++) {
  const name = prompt("Anna koiran nimi:");
  dogs.push(name);
}

dogs.sort().reverse();

let html = "";
for (let i = 0; i < dogs.length; i++) {
  html += `<li>${dogs[i]}</li>`;
}

document.querySelector("#target").innerHTML = html;