"use strict";
/*
function fruitProcessor(x) {
  // const juice = `${x} juice is ready`;
  // return juice;
  return `${x} juice is ready`;
}

const f1 = fruitProcessor("apple");
const f2 = fruitProcessor("orange");
const f3 = fruitProcessor("grape");

console.log(f1, f2, f3);
console.log(
  fruitProcessor("apple"),
  fruitProcessor("orange"),
  fruitProcessor("grape")
);
*/

/*
// function declaration
function fruitProcessor(x) {
  return `${x} juice is ready`;
}
const f1 = fruitProcessor("apple");
console.log("f1 o/p is ", f1);

// function expression
const f2 = function (x) {
  return `${x} juice is ready`;
};
const v2 = f2("orange");
console.log("f2 o/p is ", v2);

//Arrow Function
const arrowFruitProcessor = (x) => `${x} juice is ready`;
const v3 = arrowFruitProcessor("grape");
console.log("f3 o/p is ", v3);
*/

// Arrays
/*
const friends = [40, "suraj", "shiva", "ram"];
const cousins = new Array(90, "navaneeth", "abishek", "aravind", "subhashini");
// console.log(friends, cousins);
console.log(friends[0], typeof friends[0]);
console.log(friends[1], typeof friends[1]);
console.log(cousins[0], typeof cousins[0]);
console.log(cousins[1], typeof cousins[1]);
// To access the element
console.log(friends[0]);
console.log(friends[friends.length - 1]);
*/
/*
// To change item in an array
const friends = ["suraj", "shiva", "ram"];
console.log(friends);
friends[2] = "pavalan";
console.log(friends);

const details = ["Balaji", 1995, 2021 - 1995];
console.log(details);
console.log(details[0], typeof details[0]);
console.log(details[1], typeof details[1]);
console.log(details[2], typeof details[2]);
*/
/*
// To add/remove item in an array
const friends = ["suraj", "shiva", "ram"];
console.log(friends);
friends.shift();
console.log(friends);
*/
/*
// To get the index of an item
const cousins = new Array("navaneeth", "abishek", "subhashini", "aravind");
console.log(cousins.includes("subhashini"));
console.log(cousins.includes("shiva"));
*/

/*
// Object vs Array
const balajiArray = [
  "Balaji",
  "Kannigesvaran",
  1995,
  ["Suraj", "Shiva", "Pavalan"],
];
const balajiObject = {
  firstName: "Balaji",
  lastName: "Kannigesvaran",
  birthYr: 1995,
  friends: ["Suraj", "Shiva", "Pavalan"],
};
*/

/*
// Dot vs Bracket Notation
const balajiObject = {
  firstName: "Balaji",
  lastName: "Kannigesvaran",
  birthYr: 1995,
  friends: ["Suraj", "Shiva", "Pavalan"],
};
console.log(balajiObject.lastName);
console.log(balajiObject["lastName"]);

console.log(
  `${balajiObject.firstName} has ${balajiObject.friends.length} friends, and his best friend is called ${balajiObject.friends[0]}`
);
*/
/*
// Object Methods
const balajiObject = {
  firstName: "Balaji",
  lastName: "Kannigesvaran",
  birthYr: 1995,
  friends: ["Suraj", "Shiva", "Pavalan"],
  hasDriversLicense: false,
  calcAge: function () {
    return 2021 - this.birthYr;
  },
  getSummary: function () {
    return `${
      this.firstName
    } is a ${this.calcAge()} year old youngster and he has ${
      this.hasDriversLicense ? "a" : "no"
    } drivers license`;
  },
};

console.log(balajiObject.getSummary());
*/

/*
// FOR LOOP
for (let rep = 1; rep <= 10; rep++) {
  console.log(`repetition ${rep}`);
}
*/
/*
const balajiObject = [
  "Balaji",
  "Kannigesvaran",
  1995,
  ["Suraj", "Shiva", "Pavalan"],
];
for (let i = 0; i < balajiObject.length; i++) {
  console.log(balajiObject[i]);
}

const st1 = "fruits";
for (let i = 0; i < st1.length; i++) {
  console.log(st1[i]);
}

const exp = [1233, 156, 4845, 213, 84, 15156, 84];
let total = 0;
let totalArr = [];
for (let i = 0; i < exp.length; i++) {
  total = total + exp[i];
  totalArr[i] = total;
}
console.log(totalArr);

const ar1 = [1, 2, 3, 4, 5, 66, 77, 88, 100];
for (let i = 0; i < ar1.length; i++) {
  if (ar1[i] === 5) {
    break;
  }
  console.log(ar1[i]);
}
*/
const ar1 = [1, 2, 3, 4, 5, 66, 77, 88, 100];
for (let i = ar1.length - 1; i >= 0; i--) {
  console.log(ar1[i]);
}
for (let exercise = 1; exercise <= 3; exercise++) {
  for (let repetition = 1; repetition <= 5; repetition++) {
    console.log(`exercise:${exercise}, repetition ${repetition}`);
  }
}

// While loop
let rep = 1;
while (rep <= 10) {
  console.log(`repetition ${rep}`);
  rep++;
}
