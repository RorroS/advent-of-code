import * as fs from 'fs';
import * as path from 'path';

const testing = false;

const output = fs
  .readFileSync(path.join(__dirname, testing ? '../input/07_example' : '../input/07'), 'utf-8')
  .trim()
  .split('\n');

function isCommand(instruction: string) {
  return instruction.startsWith('$');
}

function isDir(instruction: string) {
  return instruction.startsWith('dir');
}

function isFile(instruction: string) {
  return Number(instruction.split(' ')[0]);
}

function parseCommand(instruction: string): { command: string; argument: string } {
  const [, command, argument] = instruction.split(' ');
  return { command, argument };
}

function sizeOfFolder(directory: string, directories: Record<string, Record<string, number>>): number {
  let size = 0;
  const dirContent = directories[directory];

  Object.entries(dirContent).forEach(([fileName, fileSize]) => {
    size += fileSize > -1 ? fileSize : sizeOfFolder(fileName, directories);
  });

  return size;
}

function parseDirectories(): Record<string, Record<string, number>> {
  const directories = {};

  let currentDir: string[] = [];
  for (let i = 0; i < output.length; i++) {
    const instr = output[i];

    if (isCommand(instr)) {
      const { command, argument } = parseCommand(instr);

      if (command === 'cd') {
        if (argument === '..') {
          currentDir = currentDir.splice(0, currentDir.length - 1);
        } else {
          currentDir.push(argument);
          directories[currentDir.join('/')] = {};
        }
      } else if (command === 'ls') {
        // do something with ls?
      }
    } else if (isDir(instr)) {
      const dirName = currentDir.join('/') + '/' + instr.split(' ')[1];
      directories[currentDir.join('/')][dirName] = -1; // -1 because why not
    } else if (isFile(instr)) {
      const [fileSize, fileName] = instr.split(' ');
      directories[currentDir.join('/')][fileName] = parseInt(fileSize);
    }
  }

  return directories;
}

function solve_part_one() {
  const directories = parseDirectories();

  let totalSize = 0;
  Object.keys(directories).forEach(dir => {
    const size = sizeOfFolder(dir, directories);
    totalSize += size <= 100_000 ? size : 0;
  });

  return totalSize;
}

function solve_part_two() {
  const directories = parseDirectories();
  const spaceRequired = 30_000_000;
  const fileSystemSize = 70_000_000;
  const spaceInUse = sizeOfFolder('/', directories);
  const availableSpace = fileSystemSize - spaceInUse;

  const candidates: number[] = [];
  Object.keys(directories).forEach(dir => {
    const folderSize = sizeOfFolder(dir, directories);
    if (availableSpace + folderSize >= spaceRequired) {
      candidates.push(folderSize);
    }
  });

  return Math.min(...candidates);
}

console.log(`p1: ${solve_part_one()}`);
console.log(`p2: ${solve_part_two()}`);
