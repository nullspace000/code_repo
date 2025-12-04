// inheritance --> allows a new class to inherit properties and methods from an existing class (parent -> child)

class Animal{
	alive = true;

	eat(){
		console.log(`This ${this.name} is eating.`);
	}
	sleeping(){
		console.log(`This ${this.name} is sleeping.`);
	}
}

class Rabbit extends Animal{
	name = "rabbit";

	run(){
		console.log(`This ${this.name} is running`);
	}
}

class Fish extends Animal{
	name = "fish";

	swim(){
		console.log(`This ${this.name} is swimming`);
	}
} 

class Hawk extends Animal{
	name = "hawk";
	
	fly(){
		console.log(`This ${this.name} is flying`);
	}
}

const rabbit = new Rabbit();
const fish = new Fish();
const hawk = new Hawk();


console.log("rabbit is alive: " + rabbit.alive);
rabbit.eat();
fish.eat();
hawk.eat();
console.log("exclusive methods:");
rabbit.run();
fish.swim();
hawk.fly();
