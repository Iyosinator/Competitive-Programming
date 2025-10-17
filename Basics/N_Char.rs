use std::io;

fn main() {
   
    let mut input = String::new();
    
    io::stdin().read_line(&mut input).unwrap();

    let ch = input.trim().chars().next().unwrap();

    if ch.is_ascii_uppercase(){
        let small = ch.to_ascii_lowercase();
        println!("{small}")
    }
    else{
        let capital = ch.to_ascii_uppercase();
        println!("{capital}")
    }  
}
