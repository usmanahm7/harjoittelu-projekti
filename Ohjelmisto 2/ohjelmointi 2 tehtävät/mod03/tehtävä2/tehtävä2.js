"use strict";

const count = parseInt(prompt("Anna osallistujien lukumäärä:"));
const names = [];

for (let i = 0; i < count; i++) {
  const name = prompt("Anna osallistujan nimi:");
  names.push(name);
}

names.sort();

let html = "";
for (let i = 0; i < names.length; i++) {
  html += `<li>${names[i]}</li>`;
}

document.querySelector("#target").innerHTML = html;