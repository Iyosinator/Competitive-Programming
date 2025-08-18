use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let t: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();

    for _ in 0..t {
        let mut x: i32 = lines.next().unwrap().unwrap().trim().parse().unwrap();
        let mut smallest = 9;

        while x > 0 {
            let digit = x % 10;
            if digit < smallest {
                smallest = digit;
            }
            x /= 10;
        }

        println!("{}", smallest);
    }
}
