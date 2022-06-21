fetch('https://cors-anywhere.herokuapp.com/https://wowmat-heroku-app.herokuapp.com/ratings')
  .then(response => response.json())
    .then(data => {
        document.getElementById('rating').innerHTML += `<span class="rating__stars" style="--rating: 5;"></span>
        <div class="rating__number">
          <span class="rating__score">${data["rating"]}</span>
          <div class="rating__reviews">${data["totalratings"]}</div>
        </div>`;
    });

