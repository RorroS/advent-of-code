import * as fs from 'fs';
import * as path from 'path';

const strategy = fs.readFileSync(path.join(__dirname, '../input/02'), 'utf-8').trim().split('\n');

interface RPS {
  [me: string]: {
    type: string;
    win: string;
    opponent: string;
    points: number;
  };
}

const MtoO: RPS = {
  X: { type: 'rock', win: 'C', opponent: 'A', points: 1 },
  Y: { type: 'paper', win: 'A', opponent: 'B', points: 2 },
  Z: { type: 'scissors', win: 'B', opponent: 'C', points: 3 }
};

interface Outcome {
  [o: string]: {
    win: string;
    lose: string;
    draw: string;
  };
}

const outcome: Outcome = {
  A: { win: 'Y', lose: 'Z', draw: 'X' },
  B: { win: 'Z', lose: 'X', draw: 'Y' },
  C: { win: 'X', lose: 'Y', draw: 'Z' }
};

function solve_part_one(): number {
  let points: number = 0;
  for (const play of strategy) {
    const [o, m] = play.split(' ');
    const myChoice = MtoO[m];
    const draw = myChoice.opponent === o;
    const win = !draw && myChoice.win === o;

    points += myChoice.points + (win ? 6 : draw ? 3 : 0);
  }
  return points;
}

function solve_part_two(): number {
  // X - lose, Y - draw, Z - win
  let points: number = 0;
  for (const play of strategy) {
    const [oChoice, o] = play.split(' ');

    if (o === 'X') {
      // Loss
      const lossChoice = outcome[oChoice].lose;
      points += MtoO[lossChoice].points;
    } else if (o === 'Y') {
      // Draw
      const drawChoice = outcome[oChoice].draw;
      points += MtoO[drawChoice].points + 3;
    } else {
      // Win
      const winChoice = outcome[oChoice].win;
      points += MtoO[winChoice].points + 6;
    }
  }

  return points;
}

console.log(`p1: ${solve_part_one()}`);
console.log(`p2: ${solve_part_two()}`);
