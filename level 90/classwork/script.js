const cards = [
    { h: "Card 1", rating: 85, img: "https://tse2.mm.bing.net/th?id=OIP.xung4mlBfvUR3RKzjnRY2AHaEK&pid=Api&P=0&h=220" },
    { h: "Card 2", rating: 60, img: "https://tse4.mm.bing.net/th?id=OIP.VJ6Han-RZj6Vl115t1FpdAHaE8&pid=Api&P=0&h=220" },
    { h: "Card 3", rating: 95, img: "https://tse3.mm.bing.net/th?id=OIP.BXYbbn0IgAucv82dsHgtzwHaEo&pid=Api&P=0&h=220" },
    { h: "Card 4", rating: 40, img: "https://tse3.mm.bing.net/th?id=OIP.U5tzWM0f7UA9VuFywxBoSQHaE8&pid=Api&P=0&h=220" },
    { h: "Card 5", rating: 70, img: "https://tse2.mm.bing.net/th?id=OIP.Rni6VTrkqpapDAyWo1RkGgHaEo&pid=Api&P=0&h=220" },
    { h: "Card 6", rating: 80, img: "https://tse2.mm.bing.net/th?id=OIP.Rni6VTrkqpapDAyWo1RkGgHaEo&pid=Api&P=0&h=220" },
];

const rnCa = (data) => {
    const cont = document.getElementById("cards");
    cont.innerHTML = "";
    data.forEach((card) => {
      const elements = document.createElement("div");
      elements.className = "card";
      elements.innerHTML = `
        <img src="${card.img}" alt="${card.h}">
        <h3>${card.h}</h3>
        <p class="rating">${card.rating}</p>
      `;
      cont.appendChild(elements);
    });
};

rnCa(cards);

document.getElementById("filter-below-average").addEventListener("click", () => {
    const average =
      cards.reduce((sum, card) => sum + card.rating, 0) / cards.length;
    const filtered = cards.filter((card) => card.rating >= average);
    rnCa(filtered);
});

document.getElementById("sort-asc").addEventListener("click", () => {
    const sorted = [...cards].sort((a, b) => a.rating - b.rating);
    rnCa(sorted);
});

document.getElementById("sort-desc").addEventListener("click", () => {
    const sorted = [...cards].sort((a, b) => b.rating - a.rating);
    rnCa(sorted);
});

document.getElementById("sort-random").addEventListener("click", () => {
    const shuffled = [...cards].sort(() => Math.random() - 0.5);
    rnCa(shuffled);
});
