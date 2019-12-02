const ADD: i32 = 1;
const MUL: i32 = 2;
const TERMINATE: i32 = 99;

fn run_intcode(code: Vec<i32>) -> Vec<i32> {
    let mut intcode_program: Vec<i32> = code.clone();

    let mut current_index = 0;
    let mut opcode = intcode_program[current_index];

    loop {
        if opcode == TERMINATE {
            break;
        }

        let val1_index = intcode_program[current_index + 1] as usize;
        let val2_index = intcode_program[current_index + 2] as usize;
        let dest_index = intcode_program[current_index + 3] as usize;

        if opcode == ADD {
            intcode_program[dest_index] = intcode_program[val1_index] + intcode_program[val2_index];
        } else if opcode == MUL {
            intcode_program[dest_index] = intcode_program[val1_index] * intcode_program[val2_index];
        } else {
            println!("WAT");
            break;
        }

        current_index += 4;
        opcode = intcode_program[current_index];
    }
    intcode_program
}

fn get_input() -> Vec<i32> {
    const INPUT: &str = include_str!("../input/2");
    let intcode: Vec<i32> = INPUT
        .trim()
        .split(",")
        .map(|x| x.parse().unwrap())
        .collect();
    intcode
}

fn solve_part_one() {
    let mut input_code: Vec<i32> = get_input();
    input_code[1] = 12;
    input_code[2] = 2;

    let res: Vec<i32> = run_intcode(input_code);

    println!("p1: {}", res[0]);
}

fn solve_part_two() {
    let input_code: Vec<i32> = get_input();
    for i in 0..100 {
        for j in 0..100 {
            let mut temp: Vec<i32> = input_code.clone();
            temp[1] = i;
            temp[2] = j;

            let res: Vec<i32> = run_intcode(temp);

            if res[0] == 19690720 {
                println!("p2: {}", 100 * res[1] + res[2]);
                break;
            }
        }
    }

}

fn main() {
    solve_part_one();
    solve_part_two();
}
