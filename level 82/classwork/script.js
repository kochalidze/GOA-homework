// 1) შევქმნათ კარტების დიზაინის მიხედვით ვებსაიტი, 
//   თითოეულ კარტაზე ჰოვერის დროს უნდა გამოვიდეს ამ კარტის შესახებ ინფორმაცია, ასევე დავამატოთ light და dark მოდი

const btn1 = document.getElementById('btn');
const btn2 = document.getElementById('btn2');
const clear = document.getElementById('clear');

btn1.addEventListener('click',  function(){

    const div1 = document.getElementById('div1')

    div1.innerHTML += `
    <p>Rezi is my frend, he is good farend. we like exercise. he is me classmate, he has blue eyes and blonde hair</p>
    `

    div1.style.backgroundColor = 'rgb(63, 10, 10)'
    div1.style.marginTop = '100pxs'
    div1.style.marginLeft = '100px'
    div1.style.width = '500px'
    div1.style.height = '400px'
    div1.style.color = 'white'
    div1.style.boxShadow = '5px 5px 5px rgb(100, 20, 15)'

})


btn2.addEventListener('click',  function(){

    const div2 = document.getElementById('div1')

    div2.innerHTML += `
    <p>Me name is giga and i am 14 years old, i like frograming and play football</p>
    `

    div2.style.backgroundColor = 'rgb(63, 10, 10)'
    div2.style.marginTop = '100pxs'
    div2.style.marginLeft = '100px'
    div2.style.width = '500px'
    div2.style.height = '400px'
    div2.style.color = 'white'
    div2.style.boxShadow = '5px 5px 5px rgb(100, 20, 15)'

})


clear.addEventListener("click", () => {
    div1.innerHTML = "";
    div2.innerHTML = "";
  });
  



