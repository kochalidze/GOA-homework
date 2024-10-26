// ---

// ### 1. **Basic Constructor**
//    - Create a constructor function `Person` that takes two parameters: `name` and `age`.
//    - Add a method `introduce()` that logs:  
//      `"Hi, I am <name> and I am <age> years old."`


//    **Example Input:**
//    ```javascript
//    const person1 = new Person('Alice', 25);
//    person1.introduce();
//    // Output: Hi, I am Alice and I am 25 years old.
//    ```
function Person(name, age) {
    this.name = name;
    this.age = age;
    this.introduce = function() {
        console.log(`Hi, I am ${this.name} and I am ${this.age} years old.`);
    };
}

// Example
const person1 = new Person('Alice', 25);
person1.introduce(); // Output: Hi, I am Alice and I am 25 years old.

// ---

// ### 2. **Constructor with Default Values**
//    - Create a constructor function `Car` with parameters `brand` and `year`.
//    - If the `year` isn't provided, set a default value of `2020`.
//    - Add a method `describe()` to print:  
//      `"This is a <brand> from <year>."`

//    **Example Input:**
//    ```javascript
//    const car1 = new Car('Toyota', 2018);
//    car1.describe(); // Output: This is a Toyota from 2018.

//    const car2 = new Car('Ford');
//    car2.describe(); // Output: This is a Ford from 2020.
//    ```

function Car(brand, year = 2020) {
    this.brand = brand;
    this.year = year;
    this.describe = function() {
        console.log(`This is a ${this.brand} from ${this.year}.`);
    };
}

// Examples
const car1 = new Car('Toyota', 2018);
car1.describe(); // Output: This is a Toyota from 2018.

const car2 = new Car('Ford');
car2.describe(); // Output: This is a Ford from 2020.

// ---

// ### 3. **Constructor with Arrays as Properties**
//    - Create a `Library` constructor that takes `name` and an array of `books`.
//    - Add a method `listBooks()` to log all books.

//    **Example Input:**
//    ```javascript
//    const myLibrary = new Library('City Library', ['1984', 'To Kill a Mockingbird']);
//    myLibrary.listBooks();
//    // Output: ['1984', 'To Kill a Mockingbird']
//    ```
function Library(name, books) {
    this.name = name;
    this.books = books;
    this.listBooks = function() {
        console.log(this.books);
        };
        }

// ---

// ### 4. **Adding Methods Inside a Constructor**
//    - Create a `Rectangle` constructor with parameters `width` and `height`.
//    - Add a method `area()` that returns the area of the rectangle.

//    **Example Input:**
//    ```javascript
//    const rect1 = new Rectangle(10, 5);
//    console.log(rect1.area()); // Output: 50
//    ```
function Rectangle(width, height) {
    this.width = width;
    this.height = height;
    this.area = function() {
        return this.width * this.height;
        };
}



// ---

// ### 5. **Constructor with Conditional Logic**
//    - Create a `Student` constructor that takes `name` and `marks` (an array of numbers).
//    - Add a method `hasPassed()` that returns `true` if the average of marks is 50 or above; otherwise, `false`.

//    **Example Input:**
//    ```javascript
//    const student1 = new Student('John', [60, 70, 80]);
//    console.log(student1.hasPassed()); // Output: true

//    const student2 = new Student('Jane', [40, 30, 45]);
//    console.log(student2.hasPassed()); // Output: false
//    ```
function Student(name, marks)  {
    this.name = name;
    this.marks = marks;
    this.hasPassed = function() {
        let sum = 0;
        for (let i = 0; i < this.marks.length; i++)   {
            sum += this.marks[i];
            }
            let average = sum / this.marks.length;
            if (average >= 50) {
                return true;
                }
                else {
                    return false;
                    }
                    }


}
// ---

// ### 6. **Using `this` to Track State**
//    - Create a `Counter` constructor with an initial value of `0`.
//    - Add methods `increment()` and `getValue()` to increase the counter by 1 and retrieve the current value, respectively.

//    **Example Input:**
//    ```javascript
//    const counter = new Counter();
//    counter.increment();
//    counter.increment();
//    console.log(counter.getValue()); // Output: 2
//    ```
function Counter() {
    this.value = 0;
    this.increment = function() {
        this.value +=  1;
        }
        this.getValue = function() {
            return this.value;
        }
}
            // 


// ---

// ### 7. **Using Objects as Constructor Parameters**
//    - Create a `Phone` constructor that takes an object parameter with `brand`, `model`, and `price`.
//    - Add a method `info()` to print the phone’s details:  
//      `"This is a <brand> <model> priced at <price> USD."`

//    **Example Input:**
//    ```javascript
//    const phone1 = new Phone({ brand: 'Apple', model: 'iPhone 13', price: 999 });
//    phone1.info(); 
//    // Output: This is an Apple iPhone 13 priced at 999 USD.
//    ```
function Phone(brand, model, price) {
    this.brand =  brand
    this.model = model
    this.price = price
    this.info = function() {
        console.log(`This is a ${this.brand} ${this.model} priced at ${this.price
            } USD.`
            );
            }
        
}

// ---