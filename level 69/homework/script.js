// Here are five sets of exercises, each related to the array methods and properties you provided. The last set combines multiple methods for more advanced tasks.

// ---

// ## **Exercise Set 1: Basics (Array Length, toString, at, join, pop, push)**
// 1. **Get Length**: Create an array with 5 items. Log the length of the array.
const numbers = [1, 2, 3, 4, 5];
console.log(numbers.length);

// 2. **Convert to String**: Convert the same array to a string using `toString()` and log the result.
const fruits = ['banana',  'apple', 'orange'];
console.log(fruits.toString());

// 3. **Access Element**: Use the `at()` method to access the second element and log it.
const cars = ['Mersedes', 'BMW', 'Brabus'];
console.log(cars.at(1));

// 4. **Join Elements**: Use `join()` to combine the array elements with `-` between them.
const colors = ['red', 'green', 'blue'];
console.log(colors.join('-'));

// 5. **Push & Pop**: Add two new elements to the array using `push()`, then remove the last element using `pop()`.
const  numbers2 = [1, 2, 3, 4, 5];
numbers2.push(20, 50, 'Kocho')
let number = numbers2.pop();
console.log(numbers2);

// ---

// ## **Exercise Set 2: Modify Array (shift, unshift, delete, concat)**
// 1. **Shift Element**: Create an array and remove the first element using `shift()`.
const array = ['apple', 'banana', 'cherry'];
console.log(array.shift());


// 2. **Unshift Element**: Add a new element at the beginning using `unshift()`.
const array2 = ['banana', 'cherry'];
console.log(array2.unshift('apple'));

// 3. **Delete Element**: Use the `delete` operator to remove the second element. Log the array and observe the result.
const countries = ["Georgia", "Braazil", "Japan", "Germany"];
delete country[0];
console.log(country);

// 4. **Concatenate Arrays**: Create two arrays and use `concat()` to merge them.
const array3 = ['apple', 'banana'];
const array4 = ['cherry', 'date'];
console.log(array3.concat(array4));

// 5. **Explore Unshift & Length**: After using `unshift()`, log the new length of the array.
const array5 = ['apple', 'banana'];
console.log(array5.unshift('cherry'));

// ---

// ## **Exercise Set 3: Searching (indexOf, lastIndexOf, includes)**
// 1. **Find Index**: Create an array with repeated values. Use `indexOf()` to find the first occurrence of an element.
// 2. **Find Last Index**: Use `lastIndexOf()` to find the last occurrence of the same element.
// 3. **Check Inclusion**: Use `includes()` to check if a specific element exists in the array.
// 4. **Invalid Index Search**: Use `indexOf()` to search for a non-existing element. Log the result.
// 5. **Case Sensitivity**: Check if `includes()` is case-sensitive by searching for different cases of the same string.

// ---

// ## **Exercise Set 4: Sorting and Reversing (sort, reverse)**
// 1. **Sort Strings**: Create an array of strings and sort them using `sort()`.
// 2. **Sort Numbers**: Create an array of numbers and sort them in ascending order.
// 3. **Custom Sort**: Use a custom comparison function to sort numbers in descending order.
// 4. **Reverse Array**: Use `reverse()` on a sorted array and log the result.
// 5. **Mix Sort and Reverse**: Sort an array, then reverse it.

// ---

// ## **Exercise Set 5: Combined Operations**
// 1. **Sort and Push**: Create an array of numbers, sort it, and add a new number using `push()`. Log the updated array.
// 2. **Concatenate and Sort**: Create two arrays, merge them with `concat()`, and sort the result.
// 3. **Push and Reverse**: Add three new elements to an array, then reverse the entire array.
// 4. **Find and Remove Element**: Use `indexOf()` to locate an element, then use `splice()` to remove it.
// 5. **Join and Include Check**: Join the elements of an array into a string, split it back into an array, and check if a specific value is included using `includes()`.

// Asceding - ზრდადობით