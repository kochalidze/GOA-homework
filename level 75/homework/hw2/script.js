// Get the input field, button, and list container elements
const itemInput = document.getElementById('itemInput');
const addButton = document.getElementById('addButton');
const itemList = document.getElementById('itemList');

// Add event listener to the button
addButton.addEventListener('click', function() {
  // Get the value from the input field
  const newItemText = itemInput.value;
  
  // Only add if the input field is not empty
  if (newItemText !== '') {
    // Create a new list item element
    const newListItem = document.createElement('li');
    newListItem.textContent = newItemText;
    
    // Append the new list item to the item list
    itemList.appendChild(newListItem);
    
    // Clear the input field after adding
    itemInput.value = '';
  } else {
    alert("Please enter an item.");
  }
});
