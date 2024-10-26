// 1. **Greeting Function**  
//    Create a function `greet` that accepts a name as a parameter and greets the person. If no name is provided, the default name should be "Guest".
function greet(name = "Guest") {
    console.log(`Hello, ${name}!`);
}

// Example usage:
greet("Alice"); // Output: Hello, Alice!
greet(); // Output: Hello, Guest!


// 2. **Addition with Default Parameters**  
//    Write a function `add_numbers` that takes two numbers and returns their sum. The second number should have a default value of 0.
function add_numbers(num1, num2 = 0) {
    return num1 + num2;
}

// Example usage:
console.log(add_numbers(5, 10)); // Output: 15
console.log(add_numbers(5)); // Output: 5


// 3. **Rectangle Area Calculator**  
//    Create a function `calculate_area` to find the area of a rectangle. It should take two parameters: length and width. If the width is not provided, use a default value of 1.
function calculate_area(length, width = 1) {
    return length * width;
}

// Example usage:
console.log(calculate_area(5, 4)); // Output: 20
console.log(calculate_area(5)); // Output: 5 (5 * 1)


// 4. **Temperature Conversion**  
//    Write a function `convert_temperature` to convert temperatures between Celsius and Fahrenheit. It should have two parameters: temperature and scale (either "C" for Celsius or "F" for Fahrenheit), with "C" as the default scale.
function convert_temperature(temperature, scale = "C") {
    if (scale === "C") {
        return (temperature * 9/5) + 32; // Convert to Fahrenheit
    } else {
        return (temperature - 32) * 5/9; // Convert to Celsius
    }
}

// Example usage:
console.log(convert_temperature(0)); // Output: 32 (C to F)
console.log(convert_temperature(32, "F")); // Output: 0 (F to C)


// 5. **Shopping List**  
//    Create a function `add_to_shopping_list` that accepts an item and a quantity. The quantity should default to 1 if not provided.
function add_to_shopping_list(item, quantity = 1) {
    console.log(`Added ${quantity} ${item}(s) to your shopping list.`);
}

// Example usage:
add_to_shopping_list("Apple", 3); // Output: Added 3 Apple(s) to your shopping list.
add_to_shopping_list("Banana"); // Output: Added 1 Banana(s) to your shopping list.



// 6. **Power Function**  
//    Write a function `power` that calculates the power of a number with a default exponent value of 2 (i.e., square).
function power(base, exponent = 2) {
    return Math.pow(base, exponent);
}

// Example usage:
console.log(power(3, 3)); // Output: 27
console.log(power(3)); // Output: 9 (3 squared)


// 7. **Personalized Message**  
//    Create a function `create_message` that generates a personalized message given a name and an optional greeting ("Hello" as default).
function create_message(name, greeting = "Hello") {
    return `${greeting}, ${name}!`;
}

// Example usage:
console.log(create_message("Alice", "Hi")); // Output: Hi, Alice!
console.log(create_message("Bob")); // Output: Hello, Bob!


// 8. **Calculate Discount**  
//    Write a function `apply_discount` that calculates the final price of an item after applying a discount. The discount should be a default of 10%.
function apply_discount(price, discount = 0.10) {
    return price - (price * discount);
}

// Example usage:
console.log(apply_discount(100)); // Output: 90
console.log(apply_discount(100, 0.20)); // Output: 80


// 9. **Introduction Function**  
//    Create a function `introduce` that takes a name, age, and country. If age and country are not provided, they should default to "unknown".
function introduce(name, age = "unknown", country = "unknown") {
    console.log(`Hi, I'm ${name}, I am ${age} years old, and I live in ${country}.`);
}

// Example usage:
introduce("Alice", 25, "USA"); // Output: Hi, I'm Alice, I am 25 years old, and I live in USA.
introduce("Bob"); // Output: Hi, I'm Bob, I am unknown years old, and I live in unknown.


// 10. **Calculate Final Price**  
//     Write a function `calculate_price` that takes the price of an item and a sales tax. The sales tax should default to 5%.
function calculate_price(price, salesTax = 0.05) {
    return price + (price * salesTax);
}

// Example usage:
console.log(calculate_price(100)); // Output: 105
console.log(calculate_price(100, 0.1)); // Output: 110


// 11. **Find the Maximum**  
//     Create a function `find_max` that accepts three numbers and returns the largest one using comparison operators and if-else statements.
function find_max(num1, num2, num3) {
    if (num1 >= num2 && num1 >= num3) {
        return num1;
    } else if (num2 >= num1 && num2 >= num3) {
        return num2;
    } else {
        return num3;
    }
}

// Example usage:
console.log(find_max(1, 5, 3)); // Output: 5


// 12. **Pass or Fail**  
//     Write a function `pass_or_fail` that accepts a student's score and returns "Pass" if the score is 50 or above, and "Fail" otherwise.
function pass_or_fail(score) {
    return score >= 50 ? "Pass" : "Fail";
}

// Example usage:
console.log(pass_or_fail(70)); // Output: Pass
console.log(pass_or_fail(40)); // Output: Fail


// 13. **Sum of Numbers**  
//     Write a function `sum_of_numbers` that accepts a list of numbers and returns their sum using a for loop.
function sum_of_numbers(numbers) {
    let sum = 0;
    for (let num of numbers) {
        sum += num;
    }
    return sum;
}

// Example usage:
console.log(sum_of_numbers([1, 2, 3, 4, 5])); // Output: 15


// 14. **Count Even Numbers**  
//     Create a function `count_evens` that accepts a list of integers and returns the count of even numbers using a for loop.
function count_evens(integers) {
    let count = 0;
    for (let num of integers) {
        if (num % 2 === 0) {
            count++;
        }
    }
    return count;
}

// Example usage:
console.log(count_evens([1, 2, 3, 4, 5, 6])); // Output: 3
