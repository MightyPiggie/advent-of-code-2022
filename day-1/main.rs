fn main() {

    read_lines();
}

use std::fs::File;
use std::io::{prelude::*, BufReader};



fn read_lines() {
    let file = File::open("input.txt").unwrap();
    let  buf_reader = BufReader::new(file);

    let mut total = 0;
    let mut vec = Vec::new();
    for line in buf_reader.lines() {
        let line = line.unwrap();
        if line.is_empty() {
            vec.push(total);
            total = 0;
        } else {
            let num: i32 = line.parse().unwrap();
            total += num;
        }
    }


    vec.sort();
    let x: i32 = vec.iter().rev().take(3).sum();

    let max_value = vec.into_iter().max().unwrap();
    
    println!("First excersice: {}", max_value);
    println!("Second excersice: {}", x);
}

