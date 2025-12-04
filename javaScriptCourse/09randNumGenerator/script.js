// random number from 1 - 6
const myButton = document.getElementById("myButton");
const myLabel = document.getElementById("myLabel");
const min = 1;
const max = 6;
let randomNum;

myButton.onclick = function(){
    randomNum = Math.floor(Math.random() * max + min);
    myLabel1.textContent = randomNum;

    randomNum = Math.floor(Math.random() * max + min);
    myLabel2.textContent = randomNum;

    randomNum = Math.floor(Math.random() * max + min);
    myLabel3.textContent = randomNum;
}