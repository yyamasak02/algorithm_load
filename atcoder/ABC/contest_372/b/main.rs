use std::io;

fn main() {
    let mut s = String::new();
    let m : i32;
    io::stdin()
        .read_line(&mut s).expect("");
    m = s.trim().parse().expect("");
    println!("{}", m);
}
