// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // Get the element with id 'red_header'
  const redHeader = document.getElementById('red_header');
  
  // Add click event listener
  redHeader.addEventListener('click', function() {
    // Add 'red' class to the header element
    document.querySelector('header').classList.add('red');
  });
});
