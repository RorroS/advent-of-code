use std::fs::File;
use std::io::{prelude::*, BufReader};

fn main() {
    let modules = get_input();

    let mut p1_total: i32 = 0;
    let mut p2_total: i32 = 0;

    for module in &modules {
        let mut current: i32 = *module;
        p1_total += get_fuel_required(current);

        loop {
            current = get_fuel_required(current);

            if current > 0 {
                p2_total += current;
            } else {
                break;
            }
        }
    }
    println!("p1: {}\np2: {}", p1_total, p2_total);
}

fn get_fuel_required(module: i32) -> i32 {
    ((module / 3) - 2) as i32
}

fn get_input() -> Vec<i32> {
    let mut lines = vec!();

    let file = File::open("../input/1").unwrap();
    let reader = BufReader::new(file);

    for line in reader.lines() {
        lines.push(line.unwrap().parse::<i32>().unwrap());
    }
    lines
}
