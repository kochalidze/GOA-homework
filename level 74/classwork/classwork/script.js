// შექმენით div ბლოკი და javascript-ისა innerHTML ატრიბუტის საშვალებით დაამატეთ რამდენიმე პარაგრაფი (მინიმუმ 3), 2 ღილაკი და სხვა თქვენთვის სასურველი ელემენტები

const meDiv = document.getElementById(`parent`);

meDiv.innerHTML += `
    <p>პარაგრაფ</p>
    <p>Goa</p>
    <p>პარაგრაფ</p>
    <button>Click me</button>
    <button>Click me</button>
    <h1>Hello</h1>
`
meDiv.style.backgroundColor = 'red';
meDiv.style.color = ' white';
