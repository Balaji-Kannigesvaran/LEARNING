// const bills = [22, 295, 176, 440, 37, 105, 10, 1100, 86, 52];
// let tip = [];
// let total = [];
// for (let i = 0; i < bills.length; i++) {
//   bills[i] >= 50 && bills[i] <= 300
//     ? (tip[i] = 0.15 * bills[i])
//     : (tip[i] = 0.2 * bills[i]);
//   total[i] = bills[i] + tip[i];
// }
// console.log(bills);
// console.log(tip);
// console.log(total);

const bills = [22, 295, 176, 440, 37, 105, 10, 1100, 86, 52];
let tips = [];
let total = [];
function calctip(bill) {
  if (bill >= 50 && bill <= 300) {
    let tip = 0.15 * bill;
    return tip;
  } else {
    let tip = 0.2 * bill;
    return tip;
  }
}

for (let i = 0; i < bills.length; i++) {
  let tip1 = calctip(bills[i]);
  tips.push(tip1);
  // total[i] = bills[i] + tip1;
  // above line can be written as belos using push
  total.push(bills[i] + tip1);
}
console.log(bills);
console.log(tips);
console.log(total);

const arr1 = [22, 295, 176, 440, 37, 105, 10, 1100, 86, 52];
function calcAvg(arr) {
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    // sum = sum + arr[i];
    sum += arr[i];
  }
  let avg = sum / arr.length;
  return avg;
}

let calcAverage = calcAvg(total);
console.log(total, calcAverage);
