const textBox = document.getElementById("textBox");
let toFarenheit = document.getElementById("toFarenheit");
let toCelsius = document.getElementById("toCelsius");
const resultDisp = document.getElementById("result");
let result = 0;

function convert(){

	if(toFarenheit.checked){
		result = textBox.value * (9/5) + 32;	
        console.log(result);
		resultDisp.textContent = result;
	}
    else if(toCelsius.checked){
		result = (textBox.value - 32) / (9/5);
        console.log(result);
		resultDisp.textContent = result;
	}
    else{
        resultDisp.textContent = 'please select a unit';
    }
    
}
