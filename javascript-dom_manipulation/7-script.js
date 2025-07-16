// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // URL to fetch movies data
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  
  // Get the list element where we'll display the movies
  const listMovies = document.getElementById('list_movies');
  
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
      // Clear any existing content in the list
      listMovies.innerHTML = '';
      
      // Loop through each movie and add it to the list
      data.results.forEach(movie => {
        const listItem = document.createElement('li');
        listItem.textContent = movie.title;
        listMovies.appendChild(listItem);
      });
    })
    .catch(error => {
      // Handle any errors that occurred during the fetch
      console.error('There was a problem with the fetch operation:', error);
      listMovies.innerHTML = '<li>Error loading movies</li>';
    });
});
