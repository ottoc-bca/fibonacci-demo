fn main() {
    let mut a: u64 = 0;
    let mut b: u64 = 1;

    println!("First 10 Fibonacci numbers:");
    for i in 0..10 {
        println!("  F({i}) = {a}");
        let next = a + b;
        a = b;
        b = next;
    }
}
