// This script will work when imported in the head tag because it waits for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // URL to fetch the French greeting
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  
  // Get the element where we'll display the greeting
  const helloElement = document.getElementById('hello');
  
  // Fetch data using the Fetch API
  fetch(url)
    .then(response => {
      // Check if the response is ok (status 200-299)
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json(); // Parse the JSON from the response
    })
    .then(data => {
      // Update the element with the greeting
      helloElement.textContent = data.hello;
    })
    .catch(error => {
      // Handle any errors that occurred during the fetch
      console.error('There was a problem with the fetch operation:', error);
      helloElement.textContent = 'Error loading greeting';
    });
});
