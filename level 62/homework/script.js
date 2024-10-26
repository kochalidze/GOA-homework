// 1.Multiply Two Numbers
// Write a function multiply() that prompts the user to input two numbers and returns their product.
function multiply() {
    num1 = prompt('Please enter first number')
    num2 = prompt('Please enter second number')

    console.log(num1 * num2)
}
multiply()


// 2.Subtract Two Numbers
// Write a function subtract() that prompts the user for two numbers and returns the difference.
function subtract() {
    num3 = prompt('Enter the first number to subtract')
    num4 = prompt('Enter the second number to subtract')

    console.log(num3 - num4)
}
subtract()

// 3.Divide Two Numbers
// Write a function divide() that prompts the user for two numbers and returns their quotient.
function divide() {
    num5 = prompt('Enter the first number to divide')
    num6 = prompt('Enter the second number to divide')

    console.log(num5 / num6)
}
divide()


// 4.Return a Full Name
// Write a function fullName() that prompts the user to input their first name and last name, and returns the full name as a single string.
function  fullName() {
    name = prompt('Enter name')
    lastname = prompt('Enter lastname')

    console.log(name + ' ' + lastname)
}
fullName()


// 5.Convert Minutes to Seconds
// Write a function minutesToSeconds() that prompts the user for a number of minutes and returns the equivalent in seconds.
function  minutesToSeconds() {
   minutes = prompt('Enter minutes')
   seconds = minutes * 60

   console.log(seconds)
}
minutesToSeconds()


// 6.Calculate the Area of a Rectangle
// Write a function rectangleArea() that prompts the user to input the length and width of a rectangle and returns the area.
function rectangleArea() {
    length = prompt('Enter length')
    width = prompt('Enter width')
    area = length * width

    console.log('area is ' + area)
}
rectangleArea()


// 7.Concatenate Two Strings
// Write a function concatenateStrings() that prompts the user for two strings and returns them concatenated together.
function concatenateStrings() {
    strings1 = prompt('Enter first string')
    strings2 = prompt('Enter second string')

    console.log(strings1 + ' ' + strings2)
}

concatenateStrings()


// 8.Exponentiation
// Write a function power() that prompts the user for a base number and an exponent, and returns the result of raising the base to the power of the exponent.
function power() {
    base = prompt('Enter base')
    exponent = prompt('Enter exponent')
    result = Math.pow(base,  exponent)
    console.log(result)
    }


// 9.Calculate Circle Circumference
// Write a function circumference() that prompts the user to input a circle's radius and returns the circumference.
function circumference() {
    radius = prompt('Enter radius');
    A = 2 * radius

    console.log('circumference is' + A)
}
circumference()


// 10.Return the Next Number
// Write a function nextNumber() that prompts the user for a number and returns the next number (the input number plus one).
function  nextNumber() {
    number = prompt('Enter number');
    next = number + 1;
    console.log(next);
}
nextNumber()
