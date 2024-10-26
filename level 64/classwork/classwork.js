const btn = document.getElementById('button')
function age() {
    let  you_age = confirm("How old are you?");
    alert(you_age)

    if(you_age == True) {
        alert("you are adult")
    } 
    else {
        alert("you are not adult")
    }
} 

age()