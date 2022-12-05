import * as fs from 'fs';
import * as path from 'path';
import { Stack } from '@datastructures-js/stack';

const [stack, procedure] = fs.readFileSync(path.join(__dirname, '../input/05'), 'utf-8').split('\n\n');

interface StackParse {
  nrOfStacks: number;
  stacks: Record<number, Stack<string>>;
}
function parseStack(): StackParse {
  const lines = stack.split('\n');
  const stacks: Record<number, Stack<string>> = {};

  const nrOfStacks = lines[lines.length - 1].replaceAll(' ', '').length;
  for (let s = 0; s < nrOfStacks; s++) {
    stacks[s] = new Stack();
  }

  for (let i = lines.length - 2; i >= 0; i--) {
    const line = lines[i];
    Object.entries(stacks).forEach(([n, s]) => {
      const stackNr = parseInt(n);
      const item = line[stackNr * 4 + 1];
      item !== ' ' && stacks[stackNr].push(item);
    });
  }
  return { nrOfStacks, stacks };
}

function solve_part_one() {
  const { nrOfStacks, stacks } = parseStack();

  const instructions = procedure.split('\n');
  for (const instruction of instructions) {
    const [, amount, , from, , to] = instruction.split(' ');

    for (let i = 0; i < parseInt(amount); i++) {
      const fromInt = parseInt(from);
      const toInt = parseInt(to);
      const popped = stacks[fromInt - 1].pop();
      stacks[toInt - 1].push(popped);
    }
  }

  let result = '';
  for (let i = 0; i < nrOfStacks; i++) {
    result += stacks[i].peek();
  }

  return result;
}

// This is dum and slow, but I'm too lazy
function solve_part_two() {
  const { nrOfStacks, stacks } = parseStack();

  const instructions = procedure.split('\n');
  for (const instruction of instructions) {
    const [, amount, , from, , to] = instruction.split(' ');
    let tempStack = [];

    let toInt = 0;
    let fromInt = 0;
    let popped = '';
    for (let i = 0; i < parseInt(amount); i++) {
      fromInt = parseInt(from);
      toInt = parseInt(to);
      popped = stacks[fromInt - 1].pop();
      tempStack.unshift(popped);
    }
    for (const p of tempStack) {
      stacks[toInt - 1].push(p);
    }
    tempStack = [];
  }

  let result = '';
  for (let i = 0; i < nrOfStacks; i++) {
    result += stacks[i].peek();
  }

  return result;
}

console.log(`p1: ${solve_part_one()}`);
console.log(`p2: ${solve_part_two()}`);
