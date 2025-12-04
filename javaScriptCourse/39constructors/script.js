// constructor --> special method for defining the properties and methods of objects
//

function Car(make,model,year,color){
	this.make = make,
	this.model = model,
	this.year = year,
	this.color = color
	this.drive = function(){console.log(`You drive the ${this.model}`)};
}

const car1 = new Car('Ford','mustang',2024,'red');
const car2 = new Car('Doge','Charger',2026,'black');

console.log(car1.make +' '+ car1.model +' '+ car1.year +' '+ car1.color);
car1.drive();

console.log(car2.make +' '+ car2.model +' '+ car2.year +' '+ car2.color);
car2.drive();

