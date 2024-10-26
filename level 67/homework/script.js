// ---

// ## **10 Simple Constructor Exercises**

// ### 1. **Basic Constructor with Properties**
//    - Create a `Person` constructor with properties `name` and `age`.  
//    - Add a method `introduce()` that logs:  
//      `"Hi, I am <name> and I am <age> years old."`
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
        }
        introduce() {
            console.log(`Hi, I am ${this.name} and I am ${this.age} years
                old.`
                );
            }


}

// ---

// ### 2. **Constructor with Default Parameter Value**
//    - Create a `Book` constructor with parameters `title` and `author`.  
//    - If no `author` is provided, set it to `"Unknown"`.  
//    - Add a method `getDetails()` to print the book's details.
class Book {
    constructor(title, author = "Unknown") {
        this.title = title;
        this.author = author;
        }
        getDetails() {
            console.log(`Title: ${this.title}, Author: ${this.author}`
                );
            }
}


// ---

// ### 3. **Constructor with Arrays**
//    - Create a `Classroom` constructor that takes an array of `students`.  
//    - Add a method `countStudents()` to log the number of students in the array.
class Classroom {
    constructor(students) {
        this.students = students;
        }
        countStudents() {
            console.log(this.students.length);
        }
}

// ---

// ### 4. **State Management with Constructor**
//    - Create a `Counter` constructor with an initial value of 0.  
//    - Add methods `increment()` and `getValue()` to increase the counter by 1 and retrieve the current value.
class Counter {
    constructor(value = 0) {
        this.value = value;
        }
        increment() {
            this.value += 1;
            }
            getValue() {
                console.log(this.value);
            }
}

// ---

// ### 5. **Constructor with Boolean State**
//    - Create a `Light` constructor with a `state` property initialized to `"off"`.  
//    - Add a method `toggle()` to switch the state between `"on"` and `"off"`.
class Light  {
    constructor(state = "off")   {
        this.state = state;
        }
        toggle() {            
            this.state === "on" ? this.state = "off" : this.state = "on"
            }
            }


// ---

// ### 6. **Product Constructor with Properties**
//    - Create a `Product` constructor with properties `name` and `price`.  
//    - Add a method `getDetails()` to log:  
//      `"Product: <name>, Price: <price> USD"`
class Product {
    constructor(name, price) {
        this.name = name;
        this.price = price;
        }
        getDetails() {
            console.log(`Product: ${this.name}, Price: ${this.price} USD`
                );
        }
}


// ---

// ### 7. **Constructor with Object Properties**
//    - Create a `User` constructor with properties `username` and `contact` (an object containing `email` and `phone`).  
//    - Add a method `getContactInfo()` to print the user’s contact information.
class User {
    constructor(username, contact) {
        this.username = username;
        this.contact = contact;
        }
        getContactInfo() {
            console.log(`Username: ${this.username}, Email: ${this.contact.email}, Phone: ${
                this.contact.phone}`
                );
            }
}


// ---

// ### 8. **Constructor with Array of Objects**
//    - Create a `Library` constructor that takes an array of book objects (each with `title` and `author`).  
//    - Add a method `listBooks()` to print all books in the library.
class Library {
    constructor(books) {
        this.books = books;
        }
        listBooks() {
            this.books.forEach(book => {
                console.log(`Title: ${book.title}, Author: ${book.author}`
                    );
                }
            );
        }
}

                    // ---


// ### 9. **Cart Constructor with Array Management**
//    - Create a `Cart` constructor with an empty `items` array.  
//    - Add methods `addItem(item)` to add an item and `getItems()` to print all items.
class Cart {
    constructor() {
        this.items = [];
        }
        addItem(item) {
            this.items.push(item);
            }
            getItems() {
                this.items.forEach(item => {
                    console.log(item);
                    }
                    );
            }
}

// ---

// ### 10. **Conditional Logic in Constructor**
//    - Create a `Student` constructor with properties `name` and `marks` (an array of numbers).  
//    - Add a method `hasPassed()` that returns `true` if the average mark is 50 or above, otherwise `false`.
class Student {
    constructor(name, marks) {
        this.name = name;
        this.marks = marks;
        }
        hasPassed() {
            const average = this.marks.reduce((a, b) => a + b, 0
            ) / this.marks.length;
            return average >= 50;
            }
}