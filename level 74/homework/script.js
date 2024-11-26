// 3) გააკეთეთ თითოეულ ნასწავლ მეთოდზე (.createElement, .appendChild(node),
// .insertBefore, .removeChild(node), .parentNode, .replaceChild) 5-5 მაგალითი,
//  ახსენით თითოეულის მუშაობა კომენტარებით.

// 1. createElement 
const newDiv = document.createElement('div');
newDiv.textContent = "This is a new div element";

document.body.appendChild(newDiv);


// 2. appendChild 
const newParagraph = document.createElement('p');
newParagraph.textContent = "This is a new paragraph";

const parentDiv = document.getElementById('parent');
parentDiv.appendChild(newParagraph);



// 3. insertBefore 
const newDiv = document.createElement('div'); 
newDiv.textContent = "This div is inserted before another element"; 

const referenceNode = document.getElementById('reference');
const parentNode = referenceNode.parentNode;

parentNode.insertBefore(newDiv, referenceNode);




// 4. removeChild 
const parentDiv1 = document.getElementById('parent'); 
const childDiv = document.getElementById('child'); 

parentDiv1.removeChild(childDiv);


// 5. parentNode
const childDiv1 = document.getElementById('child');

const parentDiv2 = childDiv1.parentNode; 

console.log(parentDiv2); 



// 6. replaceChild
const parentDiv5 = document.getElementById('parent');
const oldDiv = document.getElementById('old'); 
const newDiv = document.createElement('div');

newDiv.textContent = "This is the new div replacing the old one"; 

parentDiv5.replaceChild(newDiv, oldDiv);
