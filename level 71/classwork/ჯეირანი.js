// შექმენით ჯეირანის თამაში, საიტზე აიღეთ 3 ღილაკი შესაბამისი არჩევანით: ქვა, ბადე, მაკრატელი. საიტზე მომხმარებელს უნდა შეეძლოს ჯეირანის წესების მქონე თამაში. გამოიყენეთ Math.random


a = document.getElementById('btn1')
b = document.getElementById('btn2')
c = document.getElementById('btn3')
 
if  (Math.random() < 0.33) {
    a.style.backgroundColor = 'green'
    } else if (Math.random() < 0.66) {
        b.style.backgroundColor = 'green'
        } else {
            c.style.backgroundColor = 'green'
            }
            