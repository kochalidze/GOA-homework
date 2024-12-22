let counter = 0;

const p = document.getElementById("paragrap");
const btn1 = document.getElementById("btn1");
const btn2 = document.getElementById("decrease");
const btn3 = document.getElementById("reset");


function updateCounter() {
    p.textContent = counter;

    if (counter > 0) {
        p.style.color = "green";
    } else if (counter < 0) {
        p.style.color = "red";
    } else {
        p.style.color = "black";
    }
}

btn1.addEventListener("click", () => {
    counter++;
    updateCounter();
});

btn2.addEventListener("click", () => {
    counter--;
    updateCounter();
});

btn3.addEventListener("click", () => {
    counter = 0;
    updateCounter();
});
