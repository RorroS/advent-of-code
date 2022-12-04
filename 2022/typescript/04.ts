import * as fs from 'fs';
import * as path from 'path';

const sections = fs.readFileSync(path.join(__dirname, '../input/04'), 'utf-8').trim().split('\n');

function solve_part_one(): number {
  let fullyCotain = 0;

  for (const s of sections) {
    const [e1, e2] = s.split(',');
    const [e1s, e1e] = e1.split('-').map(s => parseInt(s));
    const [e2s, e2e] = e2.split('-').map(s => parseInt(s));

    if ((e1s >= e2s && e1e <= e2e) || (e1s <= e2s && e1e >= e2e)) {
      fullyCotain += 1;
    }
  }

  return fullyCotain;
}

function solve_part_two(): number {
  let overlapping = 0;

  for (const s of sections) {
    const [e1, e2] = s.split(',');
    const [e1s, e1e] = e1.split('-').map(s => parseInt(s));
    const [e2s, e2e] = e2.split('-').map(s => parseInt(s));

    if (
      (e2s >= e1s && e2s <= e1e) ||
      (e2e <= e1e && e2e >= e1s) ||
      (e1s >= e2s && e1s <= e2e) ||
      (e1e >= e2s && e1e <= e2e)
    ) {
      overlapping += 1;
    }
  }

  return overlapping;
}

console.log(`p1: ${solve_part_one()}`);
console.log(`p2: ${solve_part_two()}`);
