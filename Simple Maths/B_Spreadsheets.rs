use regex::Regex;
use std::io::{self,BufRead};


fn col_to_letters(mut col: usize) -> String {
    let mut letters = Vec::new();
    while col > 0 {
        col -= 1;
        letters.push((b'A' + (col % 26) as u8) as char);
        col /= 26;
    }
    letters.iter().rev().collect()
}

fn letters_to_col(letters: &str) -> usize {
    letters.chars().fold(0, |acc, c| acc * 26 + (c as usize - 'A' as usize + 1))
}

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    
    let n: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();
    
    let rxcy_re = Regex::new(r"^R(\d+)C(\d+)$").unwrap();
    let a1_re = Regex::new(r"^([A-Z]+)(\d+)$").unwrap();
    
    for _ in 0..n {
        let line = lines.next().unwrap().unwrap();
        if let Some(cap) = rxcy_re.captures(&line) {
            let row: usize = cap[1].parse().unwrap();
            let col: usize = cap[2].parse().unwrap();
            let col_letters = col_to_letters(col);
            println!("{}{}", col_letters, row);
        } else if let Some(cap) = a1_re.captures(&line) {
            let letters = &cap[1];
            let row: usize = cap[2].parse().unwrap();
            let col = letters_to_col(letters);
            println!("R{}C{}", row, col);
        }
    }
}
