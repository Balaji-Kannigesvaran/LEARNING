// Remember, we're gonna use strict mode in all scripts now!
"use strict";
function printForecast(arr) {
  let op = "...";
  for (let i = 0; i < arr.length; i++) {
    op = op + ` ${arr[i]}C in ${i + 1} days...`;
  }
  return op;
}

const arr1 = [17, 21, 23];
const arr2 = [12, 5, -5, 0, 4];
const st1 = printForecast(arr2);
console.log(st1);
