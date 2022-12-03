import * as fs from 'fs';
import * as path from 'path';

const rucksacks = fs.readFileSync(path.join(__dirname, '../input/03'), 'utf-8').trim().split('\n');

const ITEMS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';

function priority(char: string) {
  return ITEMS.indexOf(char) + 1;
}

// This assumes no character appears twice
function findCommonChars(s1: string, s2: string): string[] {
  const commons: string[] = [];
  for (const c of s1) {
    if (s2.includes(c)) commons.push(c);
  }
  return commons;
}

function findBadge(elfGroup: string[]): string | undefined {
  const [elf1, elf2, elf3] = elfGroup;

  const e1e2Commons = findCommonChars(elf1, elf2).join('');
  const e2e3Commons = findCommonChars(elf2, elf3).join('');
  const badge = findCommonChars(e1e2Commons, e2e3Commons);
  return badge[0];
}

function solve_part_one(): number | undefined {
  let sum = 0;
  for (const sack of rucksacks) {
    const first = sack.slice(0, sack.length / 2);
    const second = sack.slice(sack.length / 2);
    const commonChars = findCommonChars(first, second);

    if (!commonChars) return;

    sum += priority(commonChars[0]);
  }

  return sum;
}

function solve_part_two(): number | undefined {
  const chunkSize = 3;
  let sum = 0;
  for (let i = 0; i < rucksacks.length; i += chunkSize) {
    const badge = findBadge(rucksacks.slice(i, i + chunkSize));

    if (!badge) return;

    sum += priority(badge);
  }

  return sum;
}

console.log(`p1: ${solve_part_one()}`);
console.log(`p2: ${solve_part_two()}`);
