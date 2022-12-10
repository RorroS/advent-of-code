import * as fs from 'fs';
import * as path from 'path';

const testing = false;

const instructions = fs
  .readFileSync(path.join(__dirname, testing ? '../input/10_example' : '../input/10'), 'utf-8')
  .trim()
  .split('\n');

const INTERESTING_CYCLES = [20, 60, 100, 140, 180, 220];
const CRT_WIDTH = 40;

class CPU {
  cycle: number = 0;
  x: number = 1;
  signalStrength: number = 0;
  crt: Record<number, string> = { 0: '', 1: '', 2: '', 3: '', 4: '', 5: '' };

  private addx(v: number) {
    this.x += v;
  }

  private wait(cycles: number) {
    while (cycles > 0) {
      const row = Math.floor(this.cycle / CRT_WIDTH);
      const pixel = this.cycle % CRT_WIDTH;

      this.crt[row] += pixel >= this.x - 1 && pixel <= this.x + 1 ? '#' : ' ';

      cycles--;
      this.cycle++;

      if (INTERESTING_CYCLES.includes(this.cycle)) {
        this.signalStrength += this.cycle * this.x;
      }
    }
  }

  run(op: string) {
    const [cmd, v] = op.split(' ');
    switch (cmd) {
      case 'noop':
        this.wait(1);
        break;
      case 'addx':
        this.wait(2);
        this.addx(parseInt(v));
        break;
    }
  }
}

function solve() {
  const cpu = new CPU();
  for (const instr of instructions) {
    cpu.run(instr);
  }

  console.log(`p1: ${cpu.signalStrength}`);
  console.log('p2:');
  Object.values(cpu.crt).map(v => {
    console.log(v);
  });
}

solve();
