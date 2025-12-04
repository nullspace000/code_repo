//spread expands string/array into elements

let numbers = [1,2,3,4,5];
let maximum = Math.max(...numbers);
console.log(maximum);

let username = 'David Martinez';
let letters = [...username].join('-');
console.log(letters);
//output --> D-a-v-i-d- -M-a-r-t-i-n-e-z

let fruits = ['apple','orange','banana'];
let vegetables = ['carrots','celery','potatoes'];
let foods = [...fruits, ...vegetables, 'eggs', 'milk'];
console.log(foods);
//output --> ['apple', 'orange','banana','carrots','celery','potatoes','eggs','milk']


// REST bundles elements into string/array
function combineStrings(...strings){
    return strings.join(' ');
}

const fullName = combineStrings('Mr.', 'Spongebob', 'Squarepants', 'III');

console.log(fullName);