
class Person{
	constructor(firstName, lastName, age){
		this.firstName = firstName;
		this.lastName = lastName; 
		this.age = age;
	}

	set firstName(newFirstName){
		if(typeof newFirstName === "string" && newFirstName.length > 0){
			this._firstName = newFirstName;
		}
		else{
			console.error("First name must be a non-empty string");
		}
	}

	set lastName(newLastName){
		if(typeof newLastName === "string" && newLastName.length > 0){
			this._lastName= newLastName;
		}
		else{
			console.error("Last name must be a non-empty string");
		}
	}

	set age(newAge){
		if(typeof newAge === "number" && newAge >= 0){
			this._age = newAge;
		}
		else{
			console.error("Age must be a non-negative number");
		}
	}

	get firstName(){
		return this._firstName;
	}

	get lastName(){
		return this._lastName;
	}

	get age(){
		return this._age;
	}
//property fullName isn't a property of person but, we can access it as if it were. This is very usefull if you don't want to create a new property/atribute.
	get fullName(){
		return (`${this._firstName} ${this._lastName}`);
	}
}

const person = new Person("Bob", "Ross" , 30);

console.log(person.firstName);
console.log(person.lastName);
console.log(person.fullName);
console.log(person.age);
