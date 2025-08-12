fn main() {
    use std::io;

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    
    let n: u64 = input.trim().parse().unwrap();
    let sum = n * (n + 1) / 2;

    println!("{sum}");
}
