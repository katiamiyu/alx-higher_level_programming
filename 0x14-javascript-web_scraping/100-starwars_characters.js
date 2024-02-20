#!/usr/bin/node

const request = require('request');
const endpoint = 'https://swapi-api.hbtn.io/api/';
const filmId = process.argv[2];
request.get(endpoint + 'films/' + filmId,
  function (err, resp, body) {
    if (err) {
      console.log(err);
    }
    const film = JSON.parse(body);
    for (const index in film.characters) {
      request.get(film.characters[index],
        function (err, resp, body) {
          if (err) {
            console.log(err);
          }
          const character = JSON.parse(body);
          console.log(character.name);
        }
      );
    }
  });
