// 3) თითეულ ნასწავლ მეთოდზე გააკეთეთ 10-10 მაგალითი
// abs
console.log(Math.abs(-10));      // 10
console.log(Math.abs(0));        // 0
console.log(Math.abs(3.5));      // 3.5
console.log(Math.abs(-8.7));     // 8.7
console.log(Math.abs(-Infinity)); // Infinity
console.log(Math.abs(Infinity));  // Infinity
console.log(Math.abs(NaN));      // NaN
console.log(Math.abs(-42));      // 42
console.log(Math.abs(4.56));     // 4.56
console.log(Math.abs(-5));       // 5


// ceil
console.log(Math.ceil(4.2));     // 5
console.log(Math.ceil(-4.2));    // -4
console.log(Math.ceil(0.1));     // 1
console.log(Math.ceil(-0.1));    // 0
console.log(Math.ceil(5));       // 5
console.log(Math.ceil(5.99));    // 6
console.log(Math.ceil(0));       // 0
console.log(Math.ceil(-0.99));   // 0
console.log(Math.ceil(Infinity)); // Infinity
console.log(Math.ceil(-Infinity)); // -Infinity


//  floor
console.log(Math.floor(4.9));     // 4
console.log(Math.floor(-4.9));    // -5
console.log(Math.floor(0.99));    // 0
console.log(Math.floor(-0.1));    // -1
console.log(Math.floor(5));       // 5
console.log(Math.floor(5.1));     // 5
console.log(Math.floor(0));       // 0
console.log(Math.floor(-0.99));   // -1
console.log(Math.floor(Infinity)); // Infinity
console.log(Math.floor(-Infinity)); // -Infinity


//   round
console.log(Math.round(4.5));     // 5
console.log(Math.round(-4.5));    // -4
console.log(Math.round(0.99));    // 1
console.log(Math.round(-0.99));   // -1
console.log(Math.round(5));       // 5
console.log(Math.round(5.1));     // 5
console.log(Math.round(5.9));     // 6
console.log(Math.round(0));       // 0
console.log(Math.round(Infinity)); // Infinity
console.log(Math.round(-Infinity)); // -Infinity

//    pow
console.log(Math.pow(2, 3));       // 8
console.log(Math.pow(5, 2));       // 25
console.log(Math.pow(10, 0));      // 1
console.log(Math.pow(2, -3));      // 0.125
console.log(Math.pow(-2, 3));      // -8
console.log(Math.pow(-2, 2));      // 4
console.log(Math.pow(0, 5));       // 0
console.log(Math.pow(3, 1.5));     // 5.196
console.log(Math.pow(Infinity, 0)); // 1
console.log(Math.pow(5, NaN));     // NaN


// max
console.log(Math.max(10, 20, 30)); // 30
console.log(Math.max(-10, -20));   // -10
console.log(Math.max(0, -10, 10)); // 10
console.log(Math.max(5, 3.5, 2.9)); // 5
console.log(Math.max(-5, -3, -7)); // -3
console.log(Math.max(1, NaN));     // NaN
console.log(Math.max(Infinity, 5)); // Infinity
console.log(Math.max(-Infinity, 5)); // 5
console.log(Math.max());            // -Infinity
console.log(Math.max(5, 8, 12, 3)); // 12


//  min
console.log(Math.min(10, 20, 30)); // 10
console.log(Math.min(-10, -20));   // -20
console.log(Math.min(0, -10, 10)); // -10
console.log(Math.min(5, 3.5, 2.9)); // 2.9
console.log(Math.min(-5, -3, -7)); // -7
console.log(Math.min(1, NaN));     // NaN
console.log(Math.min(Infinity, 5)); // 5
console.log(Math.min(-Infinity, 5)); // -Infinity
console.log(Math.min());            // Infinity
console.log(Math.min(5, 8, 12, 3)); // 3


// sqrt
console.log(Math.sqrt(9));         // 3
console.log(Math.sqrt(16));        // 4
console.log(Math.sqrt(0));         // 0
console.log(Math.sqrt(1));         // 1
console.log(Math.sqrt(2));         // 1.414
console.log(Math.sqrt(25));        // 5
console.log(Math.sqrt(Infinity));  // Infinity
console.log(Math.sqrt(-1));        // NaN
console.log(Math.sqrt(0.25));      // 0.5
console.log(Math.sqrt(100));       // 10


// random
console.log(Math.random());        // [0, 1) შორის შემთხვევითი რიცხვი
console.log(Math.random() * 10);   // [0, 10) შორის შემთხვევითი რიცხვი
console.log(Math.random() * 100);  // [0, 100) შორის შემთხვევითი რიცხვი
console.log(Math.floor(Math.random() * 6) + 1); // 1-დან 6-მდე მთელი რიცხვი
console.log(Math.floor(Math.random() * 100)); // [0, 100) მთელი რიცხვი
console.log(Math.round(Math.random() * 100)); // [0, 100] შორის შემთხვევითი რიცხვი
console.log(Math.ceil(Math.random() * 10)); // [1, 10] შორის მთელი რიცხვი
console.log(Math.random().toFixed(2));      // 2 ციფრით შემცველი შემთხვევითი რიცხვი
console.log(Math.random().toFixed(3));      // 3 ციფრით შემცველი შემთხვევითი რიცხვი
console.log(Math.floor(Math.random() * 50) + 50); // [50, 100) მთელი რიცხვი


// trunc
console.log(Math.trunc(4.9));       // 4
console.log(Math.trunc(-4.9));      // -4
console.log(Math.trunc(0.99));      // 0
console.log(Math.trunc(-0.99));     // 0
console.log(Math.trunc(5));         // 5
console.log(Math.trunc(5.1));       // 5
console.log(Math.trunc(5.9));       // 5
console.log(Math.trunc(-5.1));      // -5
console.log(Math.trunc(Infinity));  // Infinity
console.log(Math.trunc(-Infinity)); // -Infinity




// 4) Write a function that generates a random number between 1 and 100 using Math.random(). Ensure the number is an integer.
function getRandomNumber() {
    return Math.floor(Math.random() * 100) + 1;
}

// Example usage
console.log(getRandomNumber());



// 5) Write a function that calculates the area of a circle given the radius using the formula πr², and use Math.PI for π.
function calculateCircleArea(radius) {
    return Math.PI * Math.pow(radius, 2);
}

// Example usage
console.log(calculateCircleArea(5));