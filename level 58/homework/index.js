// 1. **Create an object**: Make an object called `car` with properties like `brand`, `model`, and `year`.
const car = {
    brand: 'Mersedes',
    model: 'cls 63 AMG',
    year: 2022
}


// 2. **Access object properties**: Using the `car` object, access the `brand` and `year` properties and print them.
const car1 = {
    brand: 'Mersedes',
    model: 'E-550',
    year: 2023,
}

console.log(car1.brand);
console.log(car1.model);
console.log(car1.year);


// 3. **Add a new property**: Add a new property `color` to the `car` object.
const car2 = {
    brand: 'Mersedes',
    model: 'E-550',
    year: 2023,
}

car2.color = 'black';

console.log(car2)


// 4. **Change a property value**: Update the `year` property of the `car` object to a new value.
const car3 = {
    brand: 'Mersedes',
    model: 'E-550',
    year: 2023,
}

car3.year = 2024;

console.log(car3)


// 5. **Delete a property**: Remove the `model` property from the `car` object.
const car4 = {
    brand: 'Mersedes',
    model: 'E-550',
    year: 2023,
}

delete car4.model;

console.log(car4)


// 6. **Create a method**: Add a method `startEngine` to the `car` object that prints "Engine started".
const car5 = {
    brand: 'Mersedes',
    model: 'E-550',
    year: 2023,
}

car5.startEngine = 5.5;

console.log(car5);


// 7. **Object inside an object**: Create a new object `owner` inside the `car` object with properties like `name` and `age`.
const car6 ={
    brand: 'Mersedes',
    model: 'E-550',
    year: 2023,
    owner:{
        name: 'John',
        age: 30,
        }
}
console.log(car6);
