import * as fs from 'fs';
import * as path from 'path';

const testing = false;

const trees = fs
  .readFileSync(path.join(__dirname, testing ? '../input/08_example' : '../input/08'), 'utf-8')
  .trim()
  .split('\n')
  .map(row => row.split('').map(n => parseInt(n)));

function getTreeLines(x: number, y: number): Record<string, number[]> {
  const left = trees[y].slice(0, x).reverse();
  const right = trees[y].slice(x + 1);
  const up: number[] = [];
  const down: number[] = [];
  for (let i = 0; i < y; i++) {
    up.unshift(trees[i][x]);
  }
  for (let j = y + 1; j < trees.length; j++) {
    down.push(trees[j][x]);
  }
  return { left, right, up, down };
}

function isVisible(x: number, y: number): boolean {
  const { left, right, up, down } = getTreeLines(x, y);

  return (
    trees[y][x] > Math.max(...left) ||
    trees[y][x] > Math.max(...right) ||
    trees[y][x] > Math.max(...up) ||
    trees[y][x] > Math.max(...down)
  );
}

function visibleInTreeLine(considered: number, treeLine: number[]): number {
  return Math.max(...treeLine) < considered
    ? treeLine.length
    : treeLine.findIndex(tree => tree >= considered) + 1;
}

function solve_part_one(): number {
  const outerPerimiter = trees[0].length * 2 + (trees.length - 2) * 2;
  let visibleTrees = outerPerimiter;
  for (let y = 1; y < trees.length - 1; y++) {
    for (let x = 1; x < trees[0].length - 1; x++) {
      visibleTrees += isVisible(x, y) ? 1 : 0;
    }
  }
  return visibleTrees;
}

function solve_part_two(): number {
  let bestScenicScore = 0;
  for (let y = 0; y < trees.length - 1; y++) {
    for (let x = 0; x < trees[0].length - 1; x++) {
      const { left, right, up, down } = getTreeLines(x, y);
      const scenicScore =
        visibleInTreeLine(trees[y][x], left) *
        visibleInTreeLine(trees[y][x], right) *
        visibleInTreeLine(trees[y][x], up) *
        visibleInTreeLine(trees[y][x], down);

      bestScenicScore = Math.max(scenicScore, bestScenicScore);
    }
  }
  return bestScenicScore;
}

console.log(`p1: ${solve_part_one()}`);
console.log(`p2: ${solve_part_two()}`);
