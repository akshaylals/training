// JSON Objects
// Creating a JSON String
var jsonString = JSON.stringify({
    name: 'Abhi',
    age: 30,
    address: {
        district: 'TVM',
        location: 'Technopark'
    }
});

console.log(jsonString);

// Parsing a JSON String
var jsonObj = JSON.parse(jsonString);
console.log(jsonObj);

