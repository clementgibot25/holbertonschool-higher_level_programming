// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // Get the toggle header button
  const toggleHeader = document.getElementById('toggle_header');
  const header = document.querySelector('header');
  
  // Add click event listener
  toggleHeader.addEventListener('click', function() {
    // Toggle between red and green classes
    if (header.classList.contains('red')) {
      header.classList.remove('red');
      header.classList.add('green');
    } else {
      header.classList.remove('green');
      header.classList.add('red');
    }
  });
});
