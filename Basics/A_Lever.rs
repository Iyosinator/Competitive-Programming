use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    
    for _ in 0..lines.next().unwrap().unwrap().trim().parse::<usize>().unwrap() {
        let _ = lines.next().unwrap().unwrap(); // skip n
        let a: Vec<i32> = lines.next().unwrap().unwrap().split_whitespace().map(|x| x.parse().unwrap()).collect();
        let b: Vec<i32> = lines.next().unwrap().unwrap().split_whitespace().map(|x| x.parse().unwrap()).collect();
        println!("{}", a.iter().zip(b.iter()).map(|(&ai, &bi)| if ai > bi { ai - bi } else { 0 }).sum::<i32>() + 1);
    }
}
