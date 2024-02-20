#!/usr/bin/node

const request = require('request');

function callback (error, response) {
  if (!error) {
    console.log(`code: ${response.statusCode}`);
  }
}

if (process.argv.length === 3) {
  const url = process.argv[2];
  request.get(url, callback);
}
