//დავალება: for-ლუპის დახმარებით ჩაწერეთ ლისტში 1-დან 30-მდე რიცხვები, და შემდეგ შექმენით ახალი ლისტი სადაც ჩაწერთ იმ ლისტში მყოფ რიცხვებიდან მარტო ლუწ რიცხვებს

const numbers = []
for (let i = 0; i  < 30 + 1; i++) {
    numbers.push(i % 2 == 0);
}  

const evenNumbers = []
for (let i = 0;  i < numbers.length; i++) {
    if  (i % 2 == 0) {
        evenNumbers.push(numbers[i])
    } 
}


