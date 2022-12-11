import * as fs from 'fs';
import * as path from 'path';

const testing = false;

const input = fs
  .readFileSync(path.join(__dirname, testing ? '../input/11_example' : '../input/11'), 'utf-8')
  .trim()
  .split('\n\n');

interface TestType {
  divBy: number;
  ifTrue: number;
  ifFalse: number;
}

interface Op {
  left: string;
  op: string;
  right: string;
}

function doOp(old: number, op: Op): number {
  const left = Number(op.left) ? parseInt(op.left) : old;
  const right = Number(op.right) ? parseInt(op.right) : old;
  switch (op.op) {
    case '+':
      return left + right;
    case '*':
      return left * right;
  }
}

class Monkey {
  items: number[];
  op: Op;
  test: TestType;
  throws: number = 0;

  constructor(items: number[], op: Op, test: TestType) {
    this.items = items;
    this.op = op;
    this.test = test;
  }

  doRound(divideWorry: number, modBy: number): number[] {
    const recipients: number[] = [];
    for (let i = 0; i < this.items.length; i++) {
      const worryLevel = Math.floor(doOp(this.items[i], this.op) / divideWorry) % modBy;

      const divisible = !(worryLevel % this.test.divBy);
      recipients.push(divisible ? this.test.ifTrue : this.test.ifFalse);
      this.items[i] = worryLevel;
      this.throws += 1;
    }
    return recipients;
  }
}

function parseMonkeys(): Monkey[] {
  const monkeys: Monkey[] = [];
  for (const monkey of input) {
    const parsed = monkey.split('\n');

    const items = parsed[1]
      .split(':')[1]
      .split(',')
      .map(i => parseInt(i));

    const [left, op, right] = parsed[2].split(':')[1].split(' = ')[1].split(' ');
    const divBy = parseInt(parsed[3].split(' ').at(-1));
    const ifTrue = parseInt(parsed[4].split(' ').at(-1));
    const ifFalse = parseInt(parsed[5].split(' ').at(-1));

    monkeys.push(new Monkey(items, { left, op, right }, { divBy, ifTrue, ifFalse }));
  }

  return monkeys;
}

function solve(rounds: number, divideWorry: number) {
  const monkeys = parseMonkeys();

  const modBy = monkeys.map(m => m.test.divBy).reduce((p, c) => p * c);

  for (let i = 0; i < rounds; i++) {
    for (const monkey of monkeys) {
      const recipients = monkey.doRound(divideWorry, modBy);
      for (let i = 0; i < recipients.length; i++) {
        monkeys[recipients[i]].items.push(monkey.items[i]);
      }
      monkey.items = [];
    }
  }

  const [first, second]: number[] = monkeys
    .map(m => m.throws)
    .sort((a, b) => b - a)
    .slice(0, 2);

  return first * second;
}

console.log(`p1: ${solve(20, 3)}`);
console.log(`p2: ${solve(10000, 1)}`);
