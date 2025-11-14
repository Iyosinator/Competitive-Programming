use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut iter = input.split_whitespace();

    let t: usize = iter.next().unwrap().parse().unwrap();

    let mut solved = 0;

    for _ in 0..t {
        let petya: i32 = iter.next().unwrap().parse().unwrap();
        let vasya: i32 = iter.next().unwrap().parse().unwrap();
        let tonya: i32 = iter.next().unwrap().parse().unwrap();

        if petya + vasya + tonya > 1 {
            solved += 1;
        }
    }

    println!("{}", solved);
}
