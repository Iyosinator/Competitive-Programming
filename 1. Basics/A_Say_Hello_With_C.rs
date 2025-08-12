use std::io;

fn main(){
    let mut s = String::new();
    io::stdin().read_line(&mut s).unwrap();
    println!("Hello, {s}")
}