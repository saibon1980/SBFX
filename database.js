// JavaScript source code
var mysql = require('mysql');

var con = mysql.createConnection({
    host: "localhost",
    user: "admin@saibonfx.com",
    password: "$Richsaibon1"
});

con.connect(function (err) {
    if (err) throw err;
    console.log("Connected!");
});