use std::io;

fn main() {
    let mut matrix = [[0; 5]; 5];

    for i in 0..5 {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let nums: Vec<i32> = input.trim().split_whitespace().map(|x| x.parse().unwrap()).collect();
        
        for j in 0..5 {
            matrix[i][j] = nums[j];
        }
    }

    for i in 0..5 {
        for j in 0..5 {
            if matrix[i][j] == 1 {
                let moves = (i as i32 - 2).abs() + (j as i32 - 2).abs();
                println!("{moves}");
            }
        }
    }
}
