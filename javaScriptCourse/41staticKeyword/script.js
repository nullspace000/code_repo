// static --> properties and methods belong the class rather than to the objects of that class


class MathUtil{
	static PI = 3.1415;
	static getDiameter(radius){
		return radius * 2;
	}
}

console.log(MathUtil.PI);
console.log(MathUtil.getDiameter(11));
