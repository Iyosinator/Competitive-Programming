use std::io::{self, BufRead};

fn letters_to_number(letters: &str) -> u32 {
    let length = letters.len() as u32;
    let mut offset = 0;
    for l in 1..length {
        offset += 26u32.pow(l);
    }
    let mut num = 0;
    for ch in letters.chars() {
        num = num * 26 + (ch as u32 - 'A' as u32);
    }
    offset + num + 1
}

fn number_to_letters(mut number: u32) -> String {
    let mut length = 1;
    loop {
        let count = 26u32.pow(length);
        if number <= count {
            break;
        }
        number -= count;
        length += 1;
    }
    number -= 1;
    let mut letters = Vec::new();
    for _ in 0..length {
        letters.push((b'A' + (number % 26) as u8) as char);
        number /= 26;
    }
    letters.iter().rev().collect()
}

fn convert(cell: &str) -> String {
    if cell.starts_with('R') && cell.contains('C') {
        // Parse R<num>C<num>
        let mut r_pos = 1;
        let chars: Vec<char> = cell.chars().collect();
        let mut row = 0u32;
        while r_pos < chars.len() && chars[r_pos].is_digit(10) {
            row = row * 10 + chars[r_pos].to_digit(10).unwrap();
            r_pos += 1;
        }
        // Skip 'C'
        let c_pos = r_pos + 1;
        let col: u32 = cell[c_pos..].parse().unwrap();
        let col_letters = number_to_letters(col);
        format!("{}{}", col_letters, row)
    } else {
        let mut i = 0;
        let chars: Vec<char> = cell.chars().collect();
        while i < chars.len() && chars[i].is_alphabetic() {
            i += 1;
        }
        let letters: String = chars[0..i].iter().collect();
        let row: u32 = cell[i..].parse().unwrap();
        let col = letters_to_number(&letters);
        format!("R{}C{}", row, col)
    }
}

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let n: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();
    for _ in 0..n {
        let cell = lines.next().unwrap().unwrap();
        println!("{}", convert(&cell));
    }
}
