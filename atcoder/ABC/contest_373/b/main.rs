use std::io;
use std::collections::HashMap;

fn main() {
    let mut m: HashMap<Option<char>, i32> = HashMap::new();
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("");
    for i in 0..25 {
        m.insert(s.get(i).expect("").to_string(), i);
    }
    println!("{:?}", m);
}
