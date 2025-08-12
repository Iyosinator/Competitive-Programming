use std::io;

fn main() {
   
    let mut input = String::new();
    
    io::stdin().read_line(&mut input).unwrap();

    let ch = input.trim().chars().next().unwrap();


    if ch.is_ascii_digit(){
        println!("IS DIGIT");
    }

    else if ch.is_ascii_alphabetic(){
        println!("ALPHA");

        if ch.is_ascii_uppercase(){
            println!("IS CAPITAL");
        }

        else{
            println!("IS SMALL");
        }
    }

  
}
