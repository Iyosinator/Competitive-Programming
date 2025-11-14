use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();

    let mut iter = input.lines();
    let t: usize = iter.next().unwrap().trim().parse().unwrap();

    for _ in 0..t {
        if let Some(word) = iter.next() {
            let len = word.len();

            if len <= 10 {
                println!("{word}");
            } else {
                let first = &word[..1];
                let last = &word[len - 1..];

                println!("{}{}{}", first, len - 2, last);
            }
        }
    }
}
