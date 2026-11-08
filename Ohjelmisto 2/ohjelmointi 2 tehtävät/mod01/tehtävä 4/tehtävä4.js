"use strict";

const name = prompt("Kirjoita nimesi:");

// Arotaan luku väliltä 1-4
const number = Math.floor(Math.random() * 4) + 1;

let house;

if (number === 1) {
  house = "Rohkelikko";
} else if (number === 2) {
  house = "Luihuinen";
} else if (number === 3) {
  house = "Puuskupuh";
} else {
  house = "Korpinkynsi";
}

document.querySelector("#target").innerHTML = `${name}, sinä olet ${house}.`;