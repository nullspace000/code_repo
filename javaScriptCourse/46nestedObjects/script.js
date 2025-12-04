// nested objects = objects inside other objects. Allows representation of more complex data structures. 
// Child object is enclosed by a parent object

//	Person{Adress{}, ContactInfo{}}
//	ShoppingCart{Keyboard{}, Mouse{}, Monitor{}}


//-- Example 1 --

const person = {
	fullName: "Spongebob Squarepants",
	age: 30,
	isStudent: true,
	hobbies: ["karate", "jellyfishing", "cooking"],
	address: {
		street: "124 Conch st.",
		city: "Bikini Bottom",
		country: "international water"
	}
}

console.log(person.fullName);
console.log(person.age);
console.log(person.isStudent);
console.log(person.hobbies);
console.log(person.address);

//accesing individual properties of nested object "address"
console.log(person.address.street);
console.log(person.address.city);
console.log(person.address.country);



//-- Example 2 --

class Person{
	constructor(name, age, ...address){
		this.name = name;
		this.age = age;
		this.address = new Address(...address);
	}
}

// In this example the "Adress" object is a child of the "Person" object.
class Address{
	constructor(street, city, coutry){
		this.street = street;
		this.city = city;
		this.country = country;
	}
}

const person1 = new Person("Spongebob",30,"1234 Conch St.","Bikini Bottom", "Int. Waters");

const person2 = new Person("Patrick",37,"1288 Conch St.","Bikini Bottom","Int. Waters");

const person3 = new Person("Squidward",45,"126 Conch St.","Bikini Bottom","Int. Waters"); 

console.log(person2.address.city);
