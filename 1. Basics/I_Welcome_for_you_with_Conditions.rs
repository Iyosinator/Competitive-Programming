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
    
    if (a>=b){
        println!("Yes")
    }
    else{
        println!("No")
    }
}
