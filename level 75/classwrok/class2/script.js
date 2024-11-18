// 2) შექმენით პროექტი სახელწოდებით todolist, გექნებათ ერთი ფორმა და ერთი დალაგებული სია, როდესაც ფორმა დადასტურდება წამოიღეთ დასამატებელი  მნიშნელობა და შექმენით ახალი li თეგი რომელსაც მიანეჭბთ დადასტურებულ მნიშვნელობას, ახალ უნიკალურ id_ს და მოვლენის მსმენელს რომელიც მოუსმენს დაკლიკების მოვლენას, როცა დაკლიკება მოხდება უნდა წაიშალოს კონკრეტულად ის ელემენტი რომელზეც მოხდა მოვლენა

const form = document.querySelector("form");
const ol = document.querySelector("ol");

let counter = 0;

form.addEventListener("submit", function(e) {
    e.preventDefault()

    const itemValue = form.item.value;

    const li = document.createElement("li");

    li.textContent = itemValue;

    li.id = `item-${counter}`;
    counter++

    ol.appendChild(li);

    ol.addEventListener("click", function() {
        todoList.removeChild(li);
    })

    todoList.appendChild(li);
    todoInput.value = "";
})