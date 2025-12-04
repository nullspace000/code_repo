// super = keyword used in classes to call the constructor or access the properties and methods of a parent (superclass)
// this = this object
// super = the parent

//defining classes
class Animal{
	constructor(name, age){
		this.name = name;
		this.age = age;
	}

	move(speed){
		console.log(`The ${this.name} moves at a speed of ${speed}km/h`);
	}
}

class Rabbit extends Animal{
	constructor(name, age, runSpeed){
		super(name, age);
		this.runSpeed = runSpeed;
	}

	run(){
		console.log(`This ${this.name} can run`);
		super.move(this.runSpeed);
		
	}
}

class Fish extends Animal{
	constructor(name, age, swimmSpeed){
		super(name, age);
		this.swimmSpeed = swimmSpeed;
	}
	swim(){
		console.log(`This ${this.name} can swim`);
		super.move(this.swimmSpeed);
	}
}

class Hawk extends Animal{
	constructor(name, age, flySpeed){
		super(name, age);
		this.flySpeed = flySpeed;
	}
	fly(){
		console.log(`This ${this.name} can fly`);
		super.move(this.flySpeed);
	}
}

//creating instances of each class
const rabbit = new Rabbit("rabbit", 1, 25);
const fish = new Fish("fish", 2, 12);
const hawk = new Hawk("hawk", 3, 50);

//accessing instance atributes and methods
console.log(rabbit.name);
console.log(rabbit.age);
console.log(rabbit.runSpeed);
rabbit.run();

console.log(fish.name);
console.log(fish.age);
console.log(fish.swimmSpeed);
fish.swim();

console.log(hawk.name);
console.log(hawk.age);
console.log(hawk.flySpeed);
hawk.fly();
