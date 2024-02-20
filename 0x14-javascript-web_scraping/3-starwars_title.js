#!/usr/bin/node

const request = require('request');

function callback (error, response) {
  if (!error) {
    const body = JSON.parse(response.body);
    console.log(body.title);
  }
}

if (process.argv.length === 3) {
  const id = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
  request.get(url, callback);
}
