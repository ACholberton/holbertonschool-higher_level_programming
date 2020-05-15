// Javascript script that fetches and lists all movies title by using this URL: https://swapi-api.hbtn.io/api/films/?format=json //
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
  if (status === 'success') {
    const titles = data.results;
    for (const movie of titles) {
      $('UL#list_movies').append('<li>' + movie.title + '<li>');
    }
  }
});
