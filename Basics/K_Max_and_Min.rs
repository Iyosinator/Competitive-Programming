use std::io;

fn main() {
   
    let mut input = String::new();
    
    io::stdin().read_line(&mut input).unwrap();

    let numbers: Vec<i64> = input
        .trim()
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();

    let min = numbers.iter().min().unwrap();
    let max = numbers.iter().max().unwrap();

    println!("{min} {max}")  
}
