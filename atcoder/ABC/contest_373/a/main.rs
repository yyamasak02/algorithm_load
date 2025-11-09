use std::io;

fn main() {
    // let String[]
    // let mut a: Vec<String> = Vec::new();
    let mut a: i32 = 0;

    // Input 12 times
    // append to list
    for i in 0..12 {
        let mut tmp = String::new();
        io::stdin().read_line(&mut tmp).expect("");
        tmp = tmp.trim().to_string();
        if tmp.len() == i+1 { a += 1 }
    }
    println!("{}", a);
}
