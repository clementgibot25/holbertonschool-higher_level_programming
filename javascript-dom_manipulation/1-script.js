// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // Get the element with id 'red_header'
  const redHeader = document.getElementById('red_header');
  
  // Add click event listener
  redHeader.addEventListener('click', function() {
    // Change the header text color to red
    document.querySelector('header').style.color = '#FF0000';
  });
});
