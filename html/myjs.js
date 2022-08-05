// // alert('Hello world');

// const a = 10;
// // a = 15

// var myName = 'Test';
// alert(myName);

// let myPlace = 'TVM';
// alert(myPlace);

// let myText = 'Abhi';
// alert(myText.length);

let str = 'Hello and Welcome';
// let part = str.slice(3, 10);
// let part = str.slice(-11, -4);
// let part = str.slice(3);
// let part = str.slice(-3);
// let part = str.substring(3, 10);
// let part = str.substr(3);
// let part = str.substr(-3);
// alert(part);

// let newText = str.replace('Hello', 'Hi')
// alert(newText);

// joining two strings using javascript
myText2 = ' Hope you are fine';
let myJoinedText = str.concat(myText2);
// alert(myJoinedText);

// alert(myText2.toUpperCase())
// alert(myText2.toLowerCase())

let text1 = '    Hi There!   ';
// alert(text1.trim())
// alert(myText2.charCodeAt(6))

var a = 3, b = 7;

var result = a + b;
// alert(result)

// evaluating th emath expression using js
var ex = eval("a * b + b + 2 + 3")
// alert(ex)


var a = 5, b = 10, c = 5;
var result = a === b;
// alert(result);

// if(a > b){
//     alert(a + ' is greater than ' + b)
// } else {
//     alert(a + ' is less than ' + b)
// }

// switch case
var day
switch (new Date().getDay()){
    case 1:
        day = 'Monday';
        break;
    case 2:
        day = 'Tuesday';
        break;
    case 3:
        day = 'Wednesday';
        break;
    case 4:
        day = 'Thursday';
        break;
    case 5:
        day = 'Friday';
        break;
    default:
        day = 'Weekend';
}
// alert(day)

// function add(a, b) {
//     return a + b;
// }

// var add = function (a, b) {
//     return a + b
// }

// var add = (a, b) => {
//     return a + b;
// }

// var add = (a, b) => a + b;

// console.log(add(3, 4));

// const myArray = [1, 2, 3]
// var array_square = myArray.map(a => a * a)
// console.log(array_square);

// myArray.forEach(e => {
//     console.log(e*e);
// });


// var myArray = ['abhi', 'subi', 'bibi']
// var myArray2 = myArray.concat('sibi')
// console.log(myArray2);


// // destructurign a js array
// // assigning each value of array to a variable
// const [first, second, ...rest] = myArray2;
// console.log(first);
// console.log(second);
// console.log(rest);

// // Javascript objects
// var student = {
//     studname: 'Abhi',
//     age: 35,
//     talk: function(){
//         alert('Hello Abhi')
//     }
// }

// alert(student.studname);
// student.studname = 'Libi'
// alert(student.studname);
// student.talk();


// var car = {};
// car.model = 'swift';
// car.stop = function(){
//     alert(this.model + ' stopped');
// }
// alert(car.model);
// car.stop()

// OOPs in js
// Like mainstream languages OOPs is simulated in js
// declaring the class
class Person {
    // declaring constructor
    constructor(name, age){
        this.name = name;
        this.age = age;
    }
    // a member fn inside the class
    greet(){
        console.log('I am ' + this.name);
    }
}

// creating objects for the class to access var and fns
var tom = new Person('Tom', 35);
tom.greet();

var jerry = new Person('Jerry', 22);
jerry.greet();