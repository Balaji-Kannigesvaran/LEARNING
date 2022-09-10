let markWt = 78;
let markHt = 1.69;
let johnWt = 92;
let johnHt = 1.95;
markBMI = markWt / markHt ** 2;
johnBMI = johnWt / johnHt ** 2;
markHigherBMI = markBMI > johnBMI;
console.log(markBMI, johnBMI, markHigherBMI);
let statusBMI;
if (markHigherBMI) {
  statusBMI = `Mark's BMI (${markBMI}) is higher than John's (${johnBMI})`;
} else {
  statusBMI = `John's BMI (${johnBMI}) is higher than Mark's (${markBMI})`;
}
console.log(statusBMI);
