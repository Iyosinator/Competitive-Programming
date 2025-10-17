use std::io;

fn main() {
   
    let mut input = String::new();
    
    io::stdin().read_line(&mut input).unwrap();

    let parts: Vec<f64> = input
        .trim()
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();

    let a = parts[0];
    let b = parts[1];
    let result = a / b;

    println!("floor {} / {} = {}", a as i32, b as i32, result.floor() as i32);
    println!("ceil {} / {} = {}", a as i32, b as i32, result.ceil() as i32);
    println!("round {} / {} = {}", a as i32, b as i32, result.round() as i32);
}
