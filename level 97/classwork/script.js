// 1) შექმენით ობიექტი და გამოიტანეთ მისი ინფორმაცია შემდეგი ფორმატით ( key: value )

let obj = {
    name: 'Giga',
    age: 14,
    lastName: 'Kochalidze'
}

for (let key in obj) {
    console.log(`${key}: ${obj[key]}`)
}




// Bonus) გააკეთეთ იგივე თუმცა გამოიტანეთ
// ინფორმაცია თუ value-ს 5-ზე ნაკლები ასო აქვს

let obj1 = {
    name: 'Giga',
    age: 14,
    lastName: 'Kochalidze'
}

for (const key in obj1) {
    if (obj1.hasOwnProperty(key)) {
        const value = obj1[key];
        if (typeof value === "string" && value.length < 5) {
            console.log(`${key}: ${value}`);
        }
    }
}