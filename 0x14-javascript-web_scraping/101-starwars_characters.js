#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/?format=json';
request(url, function (response, body) {
  const film = (JSON.parse(body.body));
  for (const id in film.characters) {
    request(film.characters[id], function (response, body) {
      const character = (JSON.parse(body.body));
      console.log(character.name);
    });
  }
});
