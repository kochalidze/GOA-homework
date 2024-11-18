// შექმენით დაულაგებელი სია პროგრამირების ენების შესახებ და ნასწავლი მეთოდების: document.createElement() და document.appendChild() საშვალებით ჩაამატეთ სიის ელემენტები, რომლებშიც ეწერება სხვადასხვა პროგრამირების ენის სახელი


const languages = ["JavaScript", "Python", "Java", "C++", "Ruby", "PHP", "Go", "Swift"];

const ul = document.createElement("ul");

languages.forEach(language => {
  const li = document.createElement("li");
  li.textContent = language;
  ul.appendChild(li);
});

document.getElementById("languages-list").appendChild(ul);