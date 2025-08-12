use std::io;

fn main() {
   
    let mut first_name = String::new();
    let mut second_name = String::new();

    io::stdin().read_line(&mut first_name).unwrap();
    io::stdin().read_line(&mut second_name).unwrap();

    let parts1: Vec<&str> = first_name.trim().split_whitespace().collect();
    let parts2: Vec<&str> = second_name.trim().split_whitespace().collect();

    let last_name1 = parts1[1];
    let last_name2 = parts2[1];

    if last_name1 == last_name2{
        println!("ARE Brothers")
    }
    else{
        println!("NOT")
    }
}
