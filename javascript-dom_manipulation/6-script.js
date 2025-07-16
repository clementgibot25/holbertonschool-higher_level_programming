// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // URL to fetch character data
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  
  // Get the character element
  const characterElement = document.getElementById('character');
  
  // Fetch data using the Fetch API with promises
  fetch(url)
    .then(response => {
      // Check if the response is ok (status 200-299)
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json(); // Parse the JSON from the response
    })
    .then(data => {
      // Update the character element with the name
      characterElement.textContent = data.name;
    })
    .catch(error => {
      // Handle any errors that occurred during the fetch
      console.error('There was a problem with the fetch operation:', error);
      characterElement.textContent = 'Error loading character data';
    });
});
