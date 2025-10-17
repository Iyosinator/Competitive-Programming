use std::io;

fn main(){

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let parts: Vec<u64> = input.split_whitespace().map(|x| x.parse::<u64>().unwrap()).collect();

    let (m,n) = (parts[0],parts[1]);

    let max = (n*m) / 2;

    println!("{max}");


}