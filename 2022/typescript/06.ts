import * as fs from 'fs';
import * as path from 'path';

const dataStreamBuffer = fs.readFileSync(path.join(__dirname, '../input/06'), 'utf-8').trim();

const examples = [
  'mjqjpqmgbljsphdztnvjfqwrcgsmlb',
  'bvwbjplbgvbhsrlpgdmjqwftvncz',
  'nppdvjthqldpwncqszvftbrmjlhg',
  'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
  'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
];

function isUnique(seq: string) {
  const nonDupes = new Set(seq.split(''));

  return nonDupes.size === seq.length;
}

function solve(inputStream: string, uniques: number) {
  let pastFour = inputStream.slice(0, uniques);

  for (let i = uniques; i < inputStream.length; i++) {
    if (isUnique(pastFour)) return i;

    pastFour = pastFour.slice(1) + inputStream[i];
  }
}

function testExamples() {
  for (const stream of examples) {
    console.log(`p1: ${solve(stream, 4)}`);
    console.log(`p2: ${solve(stream, 14)}`);
  }
}

console.log(`p1: ${solve(dataStreamBuffer, 4)}`);
console.log(`p2: ${solve(dataStreamBuffer, 14)}`);
