// class = structured and clean way to work with objects compared to traditional constructor functions
// ex. static keyword, encapsulation, inheritance


class Product{
	constructor(name, price){
		this.name = name;
		this.price = price;
	}

	displayProduct(){
		console.log(`Product: ${this.name}`);
		console.log(`Price: ${this.price}`);
	}
}

const product1 = new Product('Shirt',19.99);
const product2 = new Product('Pants',22.50);
const product3 = new Product('Underwear',100.00);

product1.displayProduct();
product2.displayProduct();
		
