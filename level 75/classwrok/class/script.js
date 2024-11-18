// 1) შექმენით ფორმა და ცხრილი, ფორმაში იქონიეთ 4 შესატანი ველი, მომხმარებლმა უნდა შემოიტანოს სახელი, იმეილი, პაროლი და ფბ ლინკი, როდესაც ფორმა დადასტურდება როგორც იცით გვერდი ავტომატურად დარეფრეშდება, გათიშეთ ეს ქმედება preventDefault() მეთოდის დახმარებით, დადასტურების შემდეგ წამოიღეთ შემოტანილი მნიშვნელობები ინფუთებიდან name ატრიბუტის დახმარებით, ყოველ დადასტურებაზე ცხრილში შექმენით ახალი რიგი და დაამატეთ ეს მნიშვნელობები, რომელიც გამოჩნდება გვერდზე

const form = document.querySelector("form");
const tbody = document.querySelector("tbody")

form.addEventListener("Register", function(e) {
    e.preventDefault();

    const email = form.email.value;
    const password = form.password.value;
    const name = form.name.value;
    const lastNAme = form.lastname.value;
    const age = form.age.value;

    const list = [email, password, name, lastNAme, age];

    const tr = document.createElement("tr");

    for  (let i = 0; i < list.length; i++) {
        const td = document.createElement("td");
        td.textContent = list[i];
        tr.appendChild(td);

    }

    form.email.value = "";
    form.password.value = "";
    form.name.value = "";
    form.lastname.value = "";
    form.age.value =  "";


    tbody.appendChild(tr)
})