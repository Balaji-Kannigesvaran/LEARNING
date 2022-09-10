// Input set 1
// const dolphinsSC1 = 96;
// const dolphinsSC2 = 108;
// const dolphinsSC3 = 89;
// const koalasSC1 = 88;
// const koalasSC2 = 91;
// const koalasSC3 = 110;
// Input set 2
// const dolphinsSC1 = 97;
// const dolphinsSC2 = 112;
// const dolphinsSC3 = 101;
// const koalasSC1 = 109;
// const koalasSC2 = 95;
// const koalasSC3 = 123;
// Input set 3
const dolphinsSC1 = 97;
const dolphinsSC2 = 112;
const dolphinsSC3 = 101;
const koalasSC1 = 109;
const koalasSC2 = 95;
const koalasSC3 = 106;

dolphinsAvg = (dolphinsSC1 + dolphinsSC2 + dolphinsSC3) / 3;
koalasAvg = (koalasSC1 + koalasSC2 + koalasSC3) / 3;
minScore = 100;
let result;
if (dolphinsAvg > koalasAvg && dolphinsAvg >= minScore) {
  result = "Winner : Dolphins";
} else if (dolphinsAvg < koalasAvg && koalasAvg >= minScore) {
  result = "Winner : Koalas";
} else if (dolphinsAvg >= minScore) {
  result = "both wins";
} else {
  ("No one wins");
}
console.log(dolphinsAvg, koalasAvg, result);
