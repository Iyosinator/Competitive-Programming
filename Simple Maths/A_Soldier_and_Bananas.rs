use std::io;

fn main(){
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let parts: Vec<i64> = input.trim().split_whitespace().map(|x| x.parse::<i64>().unwrap()).collect();

    let k = parts[0];
    let n = parts[1];
    let w = parts[2];

    let total =  k * w * (w + 1) / 2;

    if n > total{
        println!("{}", 0)
    }
    else{
        println!("{}", total - n)
    }
}