'use strict';
/*
console.log(document.querySelector('.message').textContent);
document.querySelector('.message').textContent = '🎉Correct Number';
console.log(document.querySelector('.message').textContent);

document.querySelector('.number').textContent = 13;
document.querySelector('.score').textContent = 20;

console.log(document.querySelector('.guess').value);
document.querySelector('.guess').value = 15;
console.log(document.querySelector('.guess').value);
*/

const maxNumber = 20;
let score = maxNumber;
let highScore = 0;

const displayMessage = function (message) {
  document.querySelector('.message').textContent = message;
};

let secretNumber = Math.round(Math.random() * maxNumber);
document.querySelector('.check').addEventListener('click', function () {
  const guessstr = document.querySelector('.guess').value;
  const guess = Number(guessstr);
  if (guessstr !== '0' && !guess) {
    displayMessage('⛔No Number');
  } else if (guess === secretNumber) {
    document.querySelector('.number').textContent = secretNumber;
    displayMessage('🎉Correct Number');
    document.querySelector('body').style.backgroundColor = '#60b347';
    document.querySelector('.number').style.width = '30rem';

    if (score > highScore) {
      highScore = score;
      document.querySelector('.highscore').textContent = highScore;
    }
  } else if (score > 1) {
    score--;
    document.querySelector('.score').textContent = score;
    displayMessage(guess > secretNumber ? '📈Too High' : '📉Too Low');
  } else {
    document.querySelector('.score').textContent = 0;
    displayMessage('😭 Game Over!!!');
    document.querySelector('body').style.backgroundColor = '#ff0000';
  }
});

document.querySelector('.again').addEventListener('click', function () {
  score = maxNumber;
  secretNumber = Math.round(Math.random() * maxNumber);
  displayMessage('Start Guessing ...');
  document.querySelector('.score').textContent = score;
  document.querySelector('.number').textContent = '?';
  document.querySelector('.guess').value = '';
  document.querySelector('body').style.backgroundColor = '#222';
  document.querySelector('.number').style.width = '15rem';
});
