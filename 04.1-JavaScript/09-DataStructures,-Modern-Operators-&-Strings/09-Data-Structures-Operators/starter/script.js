'use strict';
/*
// Data needed for a later exercise
const flights =
  '_Delayed_Departure;fao93766109;txl2133758440;11:25+_Arrival;bru0943384722;fao93766109;11:45+_Delayed_Arrival;hel7439299980;fao93766109;12:05+_Departure;fao93766109;lis2323639855;12:30';

// Data needed for first part of the section
const restaurant = {
  name: 'Classico Italiano',
  location: 'Via Angelo Tavanti 23, Firenze, Italy',
  categories: ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'],
  starterMenu: ['Focaccia', 'Bruschetta', 'Garlic Bread', 'Caprese Salad'],
  mainMenu: ['Pizza', 'Pasta', 'Risotto'],

  openingHours: {
    thu: {
      open: 12,
      close: 22,
    },
    fri: {
      open: 11,
      close: 23,
    },
    sat: {
      open: 0, // Open 24 hours
      close: 24,
    },
  },
  orderDelivery: function ({
    starterIndex = 1,
    mainIndex = 1,
    time = '20:00',
    address,
  }) {
    console.log(
      `Order Received! ${this.starterMenu[starterIndex]} and ${this.mainMenu[mainIndex]} will be delivered to ${address} at ${time}`
    );
  },
};
*/

/*
const obj1 = {
  address: '4,Mainroad',
  starterIndex: 2,
};
restaurant.orderDelivery(obj1);

const {
  openingHours: {
    fri: { open: fridayOpeningHour, close: fridayClosingHour },
  },
} = restaurant;
console.log(fridayOpeningHour, fridayClosingHour);
*/

// const {
//   name: restaurantName,
//   openingHours: hours,
//   categories: tags,
// } = restaurant;
/*
const { name, openingHours, categories } = restaurant;
console.log(name, openingHours, categories);

const {
  name: restaurantName,
  openingHours: hours,
  categories: tags,
} = restaurant;
console.log(restaurantName, hours, tags);
*/

/*
const { menu: mainmenu = [], starterMenu: starter = [] } = restaurant;
console.log(mainmenu, starter);

// Mutuating Variables
let a = 111;
let b = 222;
console.log(a, b);
const obj1 = { a: 23, b: 7, c: 14 };
({ a, b } = obj1);
console.log(a, b);
({ a, b } = { b, a });
console.log(a, b);
*/

/*
const arr = [7, 8, 9];
// const badNewArr = [1, 2, arr[0], arr[1], arr[2], 3, 4];
// console.log(badNewArr);
const goodNewArr = [1, 2, ...arr, 3, 4];
const newArr = [1, 2, arr, 3, 4];
console.log(goodNewArr);
console.log(...goodNewArr);

// spread operator in function arguements
const fn1 = function (a, b, c) {
  const sum = a + b + c;
  console.log(sum);
};

const arr1 = [7, 8, 9];
fn1(arr1[0], arr1[1], arr1[2]);
fn1(...arr1);

const restaurant1 = {
  name: 'Classico Italiano',
  location: 'Via Angelo Tavanti 23, Firenze, Italy',
  categories: ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'],
  starterMenu: ['Focaccia', 'Bruschetta', 'Garlic Bread', 'Caprese Salad'],
  mainMenu: ['Pizza', 'Pasta', 'Risotto'],

  openingHours: {
    thu: {
      open: 12,
      close: 22,
    },
    fri: {
      open: 11,
      close: 23,
    },
    sat: {
      open: 0, // Open 24 hours
      close: 24,
    },
  },
};
const newRestaurant = { foundedIn: 1988, ...restaurant1, founder: 'Giuseppe' };
console.log(newRestaurant);
*/

/*
const arr1 = [1, 2, 3, 4, 5];
const arr2 = [6, 7, 8, 9, 10];
const [a, , , d, ...others] = [...arr1, ...arr2];
console.log(a, d, others);

const restaurant2 = {
  name: 'Classico Italiano',
  location: 'Via Angelo Tavanti 23, Firenze, Italy',
  categories: ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'],
  starterMenu: ['Focaccia', 'Bruschetta', 'Garlic Bread', 'Caprese Salad'],
  mainMenu: ['Pizza', 'Pasta', 'Risotto'],

  openingHours: {
    thu: {
      open: 12,
      close: 22,
    },
    fri: {
      open: 11,
      close: 23,
    },
    sat: {
      open: 0, // Open 24 hours
      close: 24,
    },
  },
};

const { sat: weekend, ...weekdays } = restaurant2.openingHours;
console.log(weekend);
console.log(weekdays);
*/

/*
const fn1 = function (...iparr) {
  let sum = 0;
  for (let i = 0; i < iparr.length; i++) {
    sum += iparr[i];
  }
  console.log(sum);
};

const arr5 = [7, 8, 9];
const arr6 = [4, 9, 7, 8, 9];
const arr7 = [6, 1, 9, 0, 5, 8, 6, 2, 9];
fn1(...arr5);
fn1(...arr6);
fn1(...arr7);
*/

/*
// Short circuiting
console.log(4 && 'Balaji');
console.log('' && 'Balaji');
console.log(true && 0);
console.log(undefined && 0);
console.log(undefined && 0 && null && 23 && 'Hello' && '');

const rest1 = {
  name: 'Capri',
  numGuests: 20,
};

const rest2 = {
  name: 'Capri',
  owner: 'Giovanni Rossi',
};

//To add numGuests if it is not available
// rest1.numGuests = rest1.numGuests || 10;
// rest2.numGuests = rest2.numGuests || 10;

rest1.numGuests ??= 10;
rest2.numGuests ??= 10;
console.log(rest1.numGuests, rest2.numGuests);

rest1.owner &&= 'Anonynous';
rest2.owner &&= 'Anonynous';
console.log(rest1.owner, rest2.owner);
*/

/*
// Challenge
const game = {
  team1: 'Bayern Munich',
  team2: 'Borrussia Dortmund',
  players: [
    [
      'Neuer',
      'Pavard',
      'Martinez',
      'Alaba',
      'Davies',
      'Kimmich',
      'Goretzka',
      'Coman',
      'Muller',
      'Gnarby',
      'Lewandowski',
    ],
    [
      'Burki',
      'Schulz',
      'Hummels',
      'Akanji',
      'Hakimi',
      'Weigl',
      'Witsel',
      'Hazard',
      'Brandt',
      'Sancho',
      'Gotze',
    ],
  ],
  score: '4:0',
  scored: ['Lewandowski', 'Gnarby', 'Lewandowski', 'Hummels'],
  date: 'Nov 9th, 2037',
  odds: {
    team1: 1.33,
    x: 3.25,
    team2: 6.5,
  },

  printGoals: function (...inpArr) {
    for (let i = 0; i < inpArr.length; i++) {
      console.log(inpArr[i], i + 1);
    }
  },
};

const [players1, players2] = game.players;

const [gk1, ...fieldPlayers1] = players1;
const [gk2, ...fieldPlayers2] = players2;
const allPlayers = [...players1, ...players2];

const players1Final = [...players1, 'Thiago', 'Countinho', 'Perisic'];

const { team1, x: draw, team2 } = game.odds;
game.printGoals(...game.scored);

team1 < team2 && console.log('Team1 is likely to win');
team1 > team2 && console.log('Team2 is likely to win');
*/

/*
const arr1 = [102, 105, 109, 116, 123];
for (let [i, el] of arr1.entries()) {
  i += 1;
  i *= 100;
  let num = i + el;
  if (num > 400 && num < 500) {
    continue;
  }
  console.log(num);
}
*/
/*
// Data needed for first part of the section
const restaurant = {
  name: 'Classico Italiano',
  location: 'Via Angelo Tavanti 23, Firenze, Italy',
  categories: ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'],
  starterMenu: ['Focaccia', 'Bruschetta', 'Garlic Bread', 'Caprese Salad'],
  mainMenu: ['Pizza', 'Pasta', 'Risotto'],

  openingHours: {
    thu: {
      open: 12,
      close: 22,
    },
    fri: {
      open: 11,
      close: 23,
    },
    sat: {
      open: 0, // Open 24 hours
      close: 24,
    },
  },
  orderDelivery: function ({
    starterIndex = 1,
    mainIndex = 1,
    time = '20:00',
    address,
  }) {
    console.log(
      `Order Received! ${this.starterMenu[starterIndex]} and ${this.mainMenu[mainIndex]} will be delivered to ${address} at ${time}`
    );
  },
};

const openingHours = {
  thu: {
    open: 12,
    close: 22,
  },
  fri: {
    open: 11,
    close: 23,
  },
  sat: {
    open: 0, // Open 24 hours
    close: 24,
  },
};

const properties = Object.entries(openingHours);
console.log(properties);

for (const [key, { open, close }] of properties) {
  console.log(`on ${key}, we can open at${open} and close at${close}`);
}
*/

/*
// Challenge
const game = {
  team1: 'Bayern Munich',
  team2: 'Borrussia Dortmund',
  players: [
    [
      'Neuer',
      'Pavard',
      'Martinez',
      'Alaba',
      'Davies',
      'Kimmich',
      'Goretzka',
      'Coman',
      'Muller',
      'Gnarby',
      'Lewandowski',
    ],
    [
      'Burki',
      'Schulz',
      'Hummels',
      'Akanji',
      'Hakimi',
      'Weigl',
      'Witsel',
      'Hazard',
      'Brandt',
      'Sancho',
      'Gotze',
    ],
  ],
  score: '4:0',
  scored: ['Lewandowski', 'Gnarby', 'Lewandowski', 'Hummels'],
  date: 'Nov 9th, 2037',
  odds: {
    team1: 1.33,
    x: 3.25,
    team2: 6.5,
  },

  printGoals: function (...inpArr) {
    for (let i = 0; i < inpArr.length; i++) {
      console.log(inpArr[i], i + 1);
    }
  },
};

const [players1, players2] = game.players;

const [gk1, ...fieldPlayers1] = players1;
const [gk2, ...fieldPlayers2] = players2;
const allPlayers = [...players1, ...players2];

const players1Final = [...players1, 'Thiago', 'Countinho', 'Perisic'];

const { team1, x: draw, team2 } = game.odds;
game.printGoals(...game.scored);

team1 < team2 && console.log('Team1 is likely to win');
team1 > team2 && console.log('Team2 is likely to win');

for (const [goal, plName] of game.scored.entries()) {
  console.log(`Goal ${goal + 1}: ${[plName]}`);
}

console.log(Object.values(game.odds));
let avg = 0;
for (const x of Object.values(game.odds)) {
  avg += x;
  avg /= Object.values(game.odds).length;
}
console.log(avg);

const odds = Object.values(game.odds);
let average = 0;
for (const odd of odds) average += odd;
average /= odds.length;
console.log(average);

for (const [team, odd] of Object.entries(game.odds)) {
  const teamStr = team === 'x' ? 'draw' : `Victory ${game[team]}`;
  console.log(`Odd of ${teamStr} ${odd}`);
}
*/

/*
const set1 = new Set([1, 1, 1, 4, 5, 4, 4, 4, 5, 8, 8, 8, 8, 6]);
const set2 = new Set('Balaji');
console.log(set1.size);
console.log(set2.size);

const setName = new Set('Balaji');
for (const letters of setName) {
  console.log(letters);
}
*/
/*
const set2 = new Set('Balaji');
const uniqueSet = set2;
const uniqueList = [...set2];
const uniqueListDirectly = [...new Set('Balaji')];
console.log(uniqueSet);
console.log(uniqueList);
console.log(uniqueListDirectly);

const list1 = [1, 1, 1, 4, 5, 4, 4, 4, 5, 8, 8, 8, 8, 6];
console.log(list1.length);
console.log(new Set(list1).size);
*/

const rest = new Map();
rest.set('name', 'Classico Italiano');
rest.set(1, 'Chennai');
rest.set(2, 'Bangalore');

rest
  .set('Categories', ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'])
  .set('Open', 11)
  .set('Close', 23)
  .set(true, 'We are Open')
  .set(false, 'We are closed');

console.log(rest.get('name'));
console.log(rest.get(true));
console.log(rest.get('true'));
console.log(rest.get(1));
console.log(rest.get('1'));

const time = 7;
console.log(rest.get(time > rest.get('Open') && time < rest.get('Close')));

console.log(rest.has('1'));
console.log(rest.has(1));

rest.delete(2);
console.log(rest);
