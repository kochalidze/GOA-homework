
const studentInfo = document.getElementById('student-info');
studentInfo.addEventListener('click', function() {
    alert('სახელი: ჯონ, გვარი: DOE');
});


const paragraphs = document.querySelectorAll('.styled-paragraph');

for (let i = 0; i < paragraphs.length; i++) {
    paragraphs[i].textContent = `Updated Paragraph ${i + 1}`;
    paragraphs[i].style.color = (i % 2 === 0) ? 'blue' : 'green';
}
