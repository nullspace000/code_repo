// object --> Collecttion of atributes and methods.
// syntax --> object = {key:value,function()}
//
// .this --> is a reference to the object we are within


const person1 = {
	firstName: 'Spongebob',
	lastName: 'Squarepants',
	age: '30',
	isEmployed: true,
	sayHello: function(){console.log(`Hi! I am ${this.firstName}`)},
	eat: function(){console.log('I am eating a krabby patty')}
};


const person2 = {
	firstName: 'Patrick',
	lastName: 'Star',
	age: 42,
	isEmployed: false,
	sayHello: () => {console.log('Hi im Patrick')},
	eat: () => {console.log('I am eating roast beef, chicken, and pizza')}
}

console.log(person1.sayHello());
console.log(person1.eat());
