import * as fs from 'fs';
import * as path from 'path';

const testing = false;

const moves = fs
  .readFileSync(path.join(__dirname, testing ? '../input/09_example' : '../input/09'), 'utf-8')
  .trim()
  .split('\n');

class Point {
  x: number;
  y: number;

  constructor(x: number, y: number) {
    this.x = x;
    this.y = y;
  }

  move(direction: string) {
    const d = directions[direction];
    this.x += d.x;
    this.y += d.y;
  }

  follow(point: Point) {
    const dirX = point.x - this.x;
    const dirY = point.y - this.y;
    const dx = Math.abs(dirX);
    const dy = Math.abs(dirY);
    const dist = Math.max(dx, dy);

    if (dist > 1) {
      this.x += dx === 2 ? dirX / 2 : dirX;
      this.y += dy === 2 ? dirY / 2 : dirY;
    }
  }
}

interface P {
  x: number;
  y: number;
}

const directions: Record<string, P> = {
  R: { x: 1, y: 0 },
  L: { x: -1, y: 0 },
  U: { x: 0, y: 1 },
  D: { x: 0, y: -1 }
};

function solve_part_one() {
  const head = new Point(0, 0);
  const tail = new Point(0, 0);
  const visited = new Set<string>().add('0,0');

  for (const move of moves) {
    const [dir, amnt] = move.split(' ');
    for (let i = 0; i < parseInt(amnt); i++) {
      head.move(dir);

      tail.follow(head);
      visited.add(`${tail.x},${tail.y}`);
    }
  }
  return visited.size;
}

function solve_part_two() {
  const knots: Point[] = [];
  for (let i = 0; i < 10; i++) {
    knots.push(new Point(0, 0));
  }

  const visited = new Set<string>().add('0,0');

  for (const move of moves) {
    const [dir, amnt] = move.split(' ');
    for (let i = 0; i < parseInt(amnt); i++) {
      knots[0].move(dir);

      for (let j = 1; j < knots.length; j++) {
        knots[j].follow(knots[j - 1]);
      }

      visited.add(`${knots[knots.length - 1].x},${knots[knots.length - 1].y}`);
    }
  }
  return visited.size;
}

console.log(`p1: ${solve_part_one()}`);
console.log(`p2: ${solve_part_two()}`);
