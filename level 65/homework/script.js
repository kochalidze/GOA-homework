// 5) კომენტარებით ახსენით რას ნიშნავს/რაში გამოიყენება dot notations - წერტილოვანი ნოტაციები 
// Dot Notation (წერტილოვანი ნოტაცია) არის JavaScript-ში ობიექტებზე არსებული თვისებების და მეთოდების წვდომის ტექნიკა. იგი გამოიყენება ობიექტის თვისებებისა და მეთოდების (ფუნქციების) მიღებისას, რაც საშუალებას გვაძლევს სწრაფად და მარტივად მივაწვდოთ ინფორმაცია კონკრეტულ ობიექტზე.




// შექმენით მარტივი პროგრამა რომელიც ცვლადში შენახული ციფრის ანუ თქვენი ასაკის მიხედვით    ითვლის ხართ თუ არა სრულწლოვანი და თუ არა მაშინ რამდენი წელიწადი გაკლიათ.

let age = 17;

function checkAge(age) {
    const legalAge = 18;
    if (age >= legalAge) {
        console.log("თქვენ ხართ სრულწლოვანი.");
    } else {
        let yearsLeft = legalAge - age;
        console.log(`თქვენ ხართ არასრულწლოვანი. თქვენ ${yearsLeft} წელი გაკლიათ სრულწლოვანების მიღწევისთვის.`);
    }
}
checkAge(age);