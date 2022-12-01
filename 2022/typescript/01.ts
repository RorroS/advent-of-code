import * as fs from 'fs';

const content = fs.readFileSync('../input/01', 'utf-8').split('\n\n');

let allCalories: number[] = [];
for (const elf of content) {
  const calories = elf
    .split('\n')
    .map(c => parseInt(c))
    .reduce((acc, curr) => acc + curr);
  allCalories.push(calories);
}

allCalories.sort((a, b) => b - a);
const topThree = allCalories.slice(0, 3).reduce((acc, curr) => acc + curr);

console.log(`p1: ${allCalories[0]}`);
console.log(`p2: ${topThree}`);
