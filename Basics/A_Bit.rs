use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let t: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();
    let mut counter = 0;

    for _ in 0..t {
        let op = lines.next().unwrap().unwrap();

        if op.starts_with('+') || op.ends_with('+') {
            counter += 1;
        } else {
            counter -= 1;
        }
    }

    println!("{}", counter);
}