use std::io;

fn main(){

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let parts: Vec<u64> = input.split_whitespace().map(|x| x.parse::<u64>().unwrap()).collect();

    let (n,m,a) = (parts[0],parts[1],parts[2]);

    let tiles_length = (n + a - 1) / a;
    let tiles_width = (m + a - 1) / a;

    println!("{}",tiles_length * tiles_width);


}