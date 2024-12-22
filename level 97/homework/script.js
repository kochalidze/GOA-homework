const emails = [
    { subject: "მოგზაურობა", content: "ნუ დაგავიწყდებათ თქვენი ბილეთები", receivedDate: "2024-12-15" },
    { subject: "მოხსენება", content: "გთხოვთ, წაიკითხოთ ბოლო ანგარიში", receivedDate: "2024-12-12" },
    { subject: "მოგზაურობა", content: "ძალიან კარგი შეთავაზება მაქვს", receivedDate: "2024-12-13" },
    { subject: "გაცნობიერება", content: "შესაძლებელია მცირე შეცდომები", receivedDate: "2024-12-10" },
    { subject: "მოგზაურობა", content: "არ დაგავიწყდეთ სასტუმროს ჯავშანი", receivedDate: "2024-12-16" }
];
  
const subjectFilter = document.getElementById("subjectFilter");
const filterButton = document.getElementById("filterButton");
const emailList = document.getElementById("emailList");

function filterEmails() {
    const selectedSubject = subjectFilter.value;
    emailList.innerHTML = "";
  
    if (!selectedSubject) {
      alert("გთხოვთ, აირჩიოთ თემა");
      return;
    }
    for (const email of emails) {
      if (email.subject === selectedSubject) {
        const li = document.createElement("li");
        li.textContent = `${email.subject}: ${email.content} (${email.receivedDate})`;
        emailList.appendChild(li);
      }
    }
}

filterButton.addEventListener("click", filterEmails);
  