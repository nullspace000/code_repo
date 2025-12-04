
let age = 0;

let myText = document.getElementById("myText");
const submitBtn = document.getElementById("mySubmit");
let resultDisp = document.getElementById("resultElement");

submitBtn.onclick = function () {
    age = myText.value;
    age = Number(age);
    if(age >= 100){
        resultDisp.textContent = "too old for this site";
    }
    else if(age >= 18){
        resultDisp.textContent = "you are old enough to visit this site";
    }
    else if(age == 0){
        resultDisp.textContent = "you were just born";
    }
    else if(age < 0){
        resultDisp.textContent = "you are can't be below 0";
    }
    else{
        resultDisp.textContent = "you must be 18+ to enter ths site";
    }
}


 
