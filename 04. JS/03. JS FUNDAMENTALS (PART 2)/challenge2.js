function calcTip(bill) {
  if (bill >= 50 && bill <= 300) {
    const tip = 0.15 * bill;
    return tip;
  } else {
    const tip = 0.2 * bill;
    return tip;
  }
}

const bill = [125, 555, 44];
const tip0 = calcTip(bill[0]);
const tot0 = bill[0] + tip0;
const tip1 = calcTip(bill[1]);
const tot1 = bill[1] + tip1;
const tip2 = calcTip(bill[2]);
const tot2 = bill[2] + tip2;
const tip = [tip0, tip1, tip2];
const tot = [tot0, tot1, tot2];

console.log(bill);
console.log(tip);
console.log(tot);

// Other method with less variables

const tips2 = [calcTip(bill[0]), calcTip(bill[1]), calcTip(bill[2])];
const total2 = [bill[0] + tips2[0], bill[1] + tips2[1], bill[2] + tips2[2]];
console.log(bill);
console.log(tips2);
console.log(total2);
