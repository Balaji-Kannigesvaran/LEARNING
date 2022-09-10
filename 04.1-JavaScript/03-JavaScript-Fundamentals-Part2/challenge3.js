const mark = {
  firstName: "Mark",
  lastName: "Miller",
  fullName: this.firstName + " " + this.lastName,
  wt: 78,
  ht: 1.69,
  calcBMI: function () {
    this.BMI = this.wt / this.ht ** 2;
    return this.BMI;
  },
};
const john = {
  firstName: "John",
  lastName: "Smith",
  fullName: this.firstName + " " + this.lastName,
  wt: 92,
  ht: 1.95,
  calcBMI: function () {
    this.BMI = this.wt / this.ht ** 2;
    return this.BMI;
  },
};
john.calcBMI();
mark.calcBMI();
console.log(john.firstName, mark.lastName, mark.fullName);
console.log(john.BMI, mark.BMI, mark.fullName);
if (john.BMI > mark.BMI) {
  console.log(
    `${john.firstName}'s BMI (${john.BMI}) is higher than ${mark.firstName}'s BMI (${mark.BMI})`
  );
} else {
  console.log(
    `${mark.firstName}'s BMI (${mark.BMI}) is higher than ${john.firstName}'s BMI (${john.BMI})`
  );
}
