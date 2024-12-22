let counter = 0;
let resetCount = 0;

const counterElement = document.getElementById("counter");
const inputValue = document.getElementById("inputValue");
const increaseButton = document.getElementById("increase");
const decreaseButton = document.getElementById("decrease");
const resetButton = document.getElementById("reset");

function updateCounter() {
    counterElement.textContent = counter;

    if (counter > 0) {
        counterElement.style.color = "green";
    } else if (counter < 0) {
        counterElement.style.color = "red";
    } else {
        counterElement.style.color = "black";
    }
}

increaseButton.addEventListener("click", () => {
    const value = parseInt(inputValue.value) || 0;

    if (value > 100) {
        alert("100-ზე მეტი რიცხვის მიმატება არ შეიძლება!");
        return;
    }

    counter += value;
    updateCounter();
});

decreaseButton.addEventListener("click", () => {
    const value = parseInt(inputValue.value) || 0;

    if (value > 100) {
        alert("100-ზე მეტი რიცხვის გამოკლება არ შეიძლება!");
        return;
    }

    counter -= value;
    updateCounter();
});

resetButton.addEventListener("click", () => {
    if (counter === 0) {
        resetCount++;
        if (resetCount > 1) {
            alert("ნოლზე უკვე ხარ და დარესტარტება აღარ შეიძლება!");
            return;
        }
    }
    counter = 0;
    updateCounter();
});
