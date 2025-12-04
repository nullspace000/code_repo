// forEach() = method used to iterate over the elements of an array and apply a specified function (callback) to each element

let numbers = [1,2,3,4,5];

numbers.forEach(double);

function double(element){
    element = element *2;
    console.log(element);
}


let fruits = ['apple','orange','banana','coconut'];

fruits.forEach(print);

function print(element){
    console.log(element);
}