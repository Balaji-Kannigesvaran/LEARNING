// Input set 1
// const dolphinsSC1 = 44;
// const dolphinsSC2 = 23;
// const dolphinsSC3 = 71;
// const koalasSC1 = 65;
// const koalasSC2 = 54;
// const koalasSC3 = 49;
// Input set 2
const dolphinsSC1 = 85;
const dolphinsSC2 = 54;
const dolphinsSC3 = 41;
const koalasSC1 = 23;
const koalasSC2 = 34;
const koalasSC3 = 27;

const calcAvg = (SC1, SC2, SC3) => (SC1 + SC2 + SC3) / 3;
const dolphinsAvg = calcAvg(dolphinsSC1, dolphinsSC2, dolphinsSC3);
const koalasAvg = calcAvg(koalasSC1, koalasSC2, koalasSC3);
console.log(dolphinsAvg, koalasAvg);

function checkWinner(team1Avg, team2Avg) {
  if (team1Avg >= 2 * team2Avg) {
    result = `Winner : Dolphins, (${team1Avg} vs ${team2Avg})`;
  } else if (team2Avg >= 2 * team1Avg) {
    result = `Winner : Koalas, (${team2Avg} vs ${team1Avg})`;
  } else {
    result = "No team wins";
  }
}
checkWinner(dolphinsAvg, koalasAvg);
console.log(result);
