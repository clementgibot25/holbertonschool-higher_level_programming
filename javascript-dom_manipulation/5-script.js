// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // Get the update header button
  const updateHeaderBtn = document.getElementById('update_header');
  
  // Add click event listener
  updateHeaderBtn.addEventListener('click', function() {
    // Update the header text
    const header = document.querySelector('header');
    header.textContent = 'New Header!!!';
  });
});
