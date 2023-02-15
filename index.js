const express = require('express');
const app = express();
app.use(express.urlencoded({extended: true}));
const mongoose = require('mongoose');
app.set('view engine', 'ejs');
var db;

mongoose.connect('mongodb://localhost:27017', {useNewUrlParser: true, useUnifiedTopology: true});
db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
  console.log("Connected to DB");
  app.listen(8080, function () {
    console.log('listening on 8080')
  });
});
var c;
    
    

app.get('/test', function(req, res) { 
  res.sendFile(__dirname +'/index.html')
})

app.get('/main', function(req, res) { 
  res.sendFile(__dirname +'/test.html')
})
