use std::io;

fn main() {
   
    let mut input = String::new();
    
    io::stdin().read_line(&mut input).unwrap();

    let parts: Vec<u64> = input
        .trim()
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();

    let a = parts[0];
    let b = parts[1];
    
   if (a > b){
        if (a%b == 0){
            println!("Multiples")
        }
        else{
            println!("No Multiples")
        }
   }
   else{
        if (b%a == 0){
            println!("Multiples")
        }
        else{
            println!("No Multiples")
        }
   }
}
