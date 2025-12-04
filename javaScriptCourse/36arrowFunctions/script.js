//arrow functions --> way to write a small function that you use once

// syntax = (parameters) => some code

const numbers = [1,2,3,4,5,6];

const squares = numbers.map((element) => Math.pow(element,2));

console.log(squares);