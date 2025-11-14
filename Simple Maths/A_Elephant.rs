use std::io;

fn main(){

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let x: i32 = input.trim().parse().unwrap();

    let result = x/5;

    if x%5 == 0 {
        println!("{}", result)
    }
    else{
         println!("{}", result + 1)
    }

}