//1) Declare a constant PI with the value 3.14 and try reassigning it. What happens?
// const myAge = 13
// myAge = 14;
// console.log(myAge)
//ვერ შევცვლით რადგან იგი მუდმივია



//2) Create a let variable age and set it to your age. Try changing it to a different value.
let age = 13;
age = 14;

console.log(age)



//3)  Declare two variables x and y using let. Assign them values and swap them without creating a new variable.
let x = 5;
let y = 10
x = 6
y = 20

console.log(x);
console.log(y);




//4)   Declare two variables x and y using let. Assign them values and swap them without creating a new variable.
let x1 = 15;
let y1 = 20;
x = 6;
y = 5;

console.log(x1);
console.log(y1);


//5) Create two variables a and b with values ​​10 and 3. Perform the following operations on them: addition, subtraction, multiplication, division, and modulus. Log the results.
let a = 10;
let b = 3;
console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);


//6) Use the exponentiation operator ** to calculate 2 raised to the power of 5. Store the result in a variable and log it.
let c = 2 ** 5;
console.log(c);


//7) Write a program that calculates the area of ​​a rectangle. Declare width and height as variables, and log the area using multiplication.
let height = 40;
let  width = 50;

console.log(height * width);


//8) Declare two numbers p and q. Perform the arithmetic operations: increment p by 1 and decrement q by 1. Log the updated values ​​of both.
let p = 5;
let q = 10;
let newP = p + 1
let newQ = q - 1
console.log(newP);
console.log(newQ);


//9) Declare two variables num1 and num2. Use comparison operators (>, <, >=, <=, ==, ===, !=, !==) to compare them. Log the results.
let num1 = 5;
let  num2 = 10;
console.log(num1 > num2);
console.log(num1 < num2);
console.log(num1 >= num2);
console.log(num1 <= num2);
console.log(num1 != num2);
console.log(num1 !== num2);
console.log(num1 == num2);
console.log(num1 === num2);


//10) Compare two strings using both == and ===. For example, compare '10' == 10 and '10' === 10. Note the difference in results.
let num3 = '20';
let bun4 = 20;
console.log(num3 == num4);
console.log(num3 === num4);

//11) Create a let variable temp and set it to 30. Write a condition that checks if temp is greater than or equal to 25. Log a message depending on the result.
let  temp = 20;
console.log(temp > 25);


//12)  Create a let variable score. Set it to 50. Write a condition that checks if the score is not equal to 100. If true, log a custom message.
let score = 50;
if (score !== 100) {
    console.log("You scored less than 100");
        } else {
            console.log("You scored 100");
            }
            
//13)  Declare a const variable myNumber and assign it a number. Check if it is of type number using typeof. Log the result.
const myNumber = 10;
console.log(typeof myNumber);


//14) Create a boolean variable isRaining and set it to false. Write a condition that logs "Take an umbrella!" if isRaining is true.
let isRaining = false;
if (isRaining) {
    console.log("Take an umbrella!");
    } else  {
        console.log("No need for an umbrella");
        }


//15) Declare a variable str and assign it a string value. Log the length of the string using .length.
let str = "Hello, World!";
console.log(str.length);


//16) Create a string variable firstName and another lastName. Concatenate them into a single variable fullName and log the result.
let firstName = "John";
let lastName = "Doe";
let fullName = firstName + " " + lastName;
console.log(fullName);


//17) Write a function that accepts two numbers, performs all arithmetic operations on them, and returns a summary object with the results (addition, subtraction, multiplication, etc.)
function mathOperations(num1, num2) {
    let summary = {
        addition: num1 + num2,
        subtraction: num1 - num2,
        multiplication: num1 * num2,
        division: num1 /  num2,
        }
        return summary;
        }


//18) Create three variables: num, isEven, and isGreaterThanTen. Set num to a number. Assign isEven a boolean based on whether the number is even, and assign isGreaterThanTen a boolean based on whether it is greater than 10.
let num = 15;
let isEven = num % 2 === 0;
let isGreaterThanTen = num > 10;


//19) Declare a let variable password and check if its length is at least 8 characters. Log "Password is strong" if the condition is met.
let password = "password123";
if (password.length >= 8) {
    console.log("Password is strong");
    } else {
        console.log("Password is weak");
        }
        

//20) Write a program that takes a string input (your name) and checks if it equals "John". If true, log "Hello, John!", else log "Hello, stranger!".
let name = "John";
