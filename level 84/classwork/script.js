
const cards = [
    {
        name: "Tbilisi",
        img: "https://tse4.mm.bing.net/th?id=OIP.jBl2DnWvDA2z4QDw8JVKggHaE8&pid=Api&P=0&h=220",
        paragrap: "Tbilisi is a sity of Georgia",
    },
    {
        name: "London",
        img: "https://tse3.mm.bing.net/th?id=OIP.2bMjEdrkxvXuvN9RyAjB9gHaEo&pid=Api&P=0&h=220",
        paragrap: "Tbilisi is a sity of Georgia", 
    },
    {
        name: "Hong Kong",
        img: "https://tse3.mm.bing.net/th?id=OIP.ZT_ZUANxnJXt7IuGdYVgkQHaEu&pid=Api&P=0&h=220",
        paragrap: "Tbilisi is a sity of Georgia",
    },
];

const div1 = document.querySelector(".parent");

cards.forEach((cards) => {
    const card = document.createElement("div");
    card.classList.add("card");

    card.innerHTML = `
    <img src="${cards.img}" alt="${cards.name}">
    <div class="card-content">
      <h2 class="card-title">${cards.name}</h2>
      <p class="card-description">${cards.paragrap}</p>
    </div>
    `

    div1.appendChild(card);
});