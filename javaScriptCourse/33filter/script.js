// .filter() = creates a new array by filtering out elements
let numbers = [1,2,3,4,5,6,7];
let evenNumbers = numbers.filter(isEven);

console.log(evenNumbers);

function isEven(element){
    return element % 2 === 0;
}



const ages = [16,17,18,18,19,20,60];
let adults = ages.filter(isAdult);

console.log(adults);

function isAdult(element){
    return element >= 18;
}




const words = ['apple','orange','bannana','kiwi','pomegranate','coconut'];

const shortWords = words.filter(getShortWords);

console.log(shortWords);

function getShortWords(element){
    return element.length <= 6;
}
