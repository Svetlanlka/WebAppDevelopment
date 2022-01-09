'use strict';

const express = require('express');
const path = require('path');
const app = express();
const htmlPath = path.resolve(__dirname, '..', 'public/index.html');
const staticPath = path.resolve(__dirname, '..', 'src');

const port = 8081;
const ip = 'http://localhost';

app.use('/', express.static(staticPath));

app.all('*', (req, res) => {
  const path_ = req.path === '/' ? 'index.html' : req.path
  res.contentType(path.basename(path_));
  console.log(req.path)
  res.sendFile(path.resolve(__dirname, '..', 'public/' + path_));
});

app.listen(port, () => {
  console.log(`listening at ${ip}:${port}`);
});
