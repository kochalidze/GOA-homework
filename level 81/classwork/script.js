// ) შევქმნათ ჯავასკრიპტით ანიმაცია რომელიც შექმნილ ოთკუდხედს შემოავლებინებს მთელ ვებსაიტს
const square = document.querySelector('.square');
const speed = 10; // ოთხკუთხედის სიჩქარე (px-ებში)

let positionX = 0; // საწყისი x კოორდინატი
let positionY = 0; // საწყისი y კოორდინატი
let directionX = 1; // x მიმართულება (1 ან -1)
let directionY = 0; // y მიმართულება (1 ან -1)

// ფანჯრის ზომის მიღება
const windowWidth = window.innerWidth;
const windowHeight = window.innerHeight;

// ანიმაციის ფუნქცია
function animateSquare() {
    // კოორდინატების განახლება
    positionX += speed * directionX;
    positionY += speed * directionY;

    // ოთკუთხედის პოზიციის განახლება
    square.style.left = positionX + 'px';
    square.style.top = positionY + 'px';

    // კედლებთან შეჯახების შემოწმება და მიმართულების შეცვლა
    if (positionX + square.clientWidth >= windowWidth && directionX === 1) {
        directionX = 0;
        directionY = 1; // ქვემოთ მოძრაობა
    } else if (positionY + square.clientHeight >= windowHeight && directionY === 1) {
        directionX = -1; // მარცხნივ მოძრაობა
        directionY = 0;
    } else if (positionX <= 0 && directionX === -1) {
        directionX = 0;
        directionY = -1; // ზემოთ მოძრაობა
    } else if (positionY <= 0 && directionY === -1) {
        directionX = 1; // მარჯვნივ მოძრაობა
        directionY = 0;
    }

    requestAnimationFrame(animateSquare);
}

// ანიმაციის დაწყება
animateSquare();
