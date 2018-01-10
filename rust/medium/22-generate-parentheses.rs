

fn generate_parenthesis(n: u32) -> Vec<String> {
    let mut results = Vec::new();
    fn generate(results: &mut Vec<String>, n: u32, s: String, left: u32, right: u32) {
        if left >= right && left < n {
            let mut s = s.clone();
            s.push('(');
            generate(results, n, s, left + 1, right);
        }
        if left >= right + 1 {
            let mut s = s.clone();
            s.push(')');
            generate(results, n, s.clone(), left, right + 1);
        }
        if left == right && left == n {
            results.push(s);
        }
    };
    generate(&mut results, n, String::with_capacity(n as usize), 0, 0);
    results
}

fn main() {
    println!("results: {:?}", generate_parenthesis(2));
    println!("results: {:?}", generate_parenthesis(3));
    println!("results: {:?}", generate_parenthesis(4));
}
