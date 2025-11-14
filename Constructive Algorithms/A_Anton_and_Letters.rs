use std::collections::HashSet;
use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let input = input.trim();

    let mut letters = HashSet::new();

    for c in input.chars() {
        if c.is_ascii_lowercase() { 
            letters.insert(c);
        }
    }

    println!("{}", letters.len());
}
