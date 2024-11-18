// შექმენით ფორმა რომელშიც მომხმარებელს შემოატანინებთ სახელს, გვარსა და ემაილს. შემდეგ ეს მონაცემები დაამატეთ ცხრილში ნასწავლი მეთოდების საშვალებით, ასევე დაამატეთ წაშლის ფუნქცია ცხრილში ელემენტზე დაჭერისას

document.getElementById("userForm").addEventListener("submit", function(event) {
    event.preventDefault(); // გვერდის გადატვირთვის თავიდან აცილება

    // ველის მნიშვნელობების ამოღება
    const firstName = document.getElementById("firstName").value;
    const lastName = document.getElementById("lastName").value;
    const email = document.getElementById("email").value;

    // ცხრილში ახალი სტრიქონის შექმნა
    const table = document.getElementById("userTable").getElementsByTagName("tbody")[0];
    const row = document.createElement("tr");

    // თითოეული მონაცემის უჯრა
    const firstNameCell = document.createElement("td");
    firstNameCell.textContent = firstName;
    row.appendChild(firstNameCell);

    const lastNameCell = document.createElement("td");
    lastNameCell.textContent = lastName;
    row.appendChild(lastNameCell);

    const emailCell = document.createElement("td");
    emailCell.textContent = email;
    row.appendChild(emailCell);

    // მოქმედებების უჯრა წაშლის ღილაკით
    const actionCell = document.createElement("td");
    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.addEventListener("click", function() {
      row.remove(); // სტრიქონის წაშლა ცხრილიდან
    });
    actionCell.appendChild(deleteButton);
    row.appendChild(actionCell);

    // ახალი სტრიქონის დამატება ცხრილში
    table.appendChild(row);

    // ველების გასუფთავება
    document.getElementById("userForm").reset();
  });