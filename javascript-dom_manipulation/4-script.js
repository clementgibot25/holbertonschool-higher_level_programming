// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // Get the button and list elements
  const addItemButton = document.getElementById('add_item');
  const myList = document.querySelector('ul.my_list');
  
  // Add click event listener to the button
  addItemButton.addEventListener('click', function() {
    // Create a new list item
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    
    // Append the new item to the list
    myList.appendChild(newItem);
  });
});
