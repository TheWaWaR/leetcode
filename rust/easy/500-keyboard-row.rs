
const ROW1: &'static str = "qwertyuiopQWERTYUIOP";
const ROW2: &'static str = "asdfghjklASDFGHJKL";
const ROW3: &'static str = "zxcvbnmZXCVBNM";

fn find_words<'a>(words: &Vec<&'a str>) -> Vec<&'a str> {
    let mut results = vec![];
    for word in words {
        let mut num: Option<usize> = None;
        for c in word.chars() {
            let n = if ROW1.find(c).is_some() {
                Some(1)
            } else if ROW2.find(c).is_some() {
                Some(2)
            } else if ROW3.find(c).is_some() {
                Some(3)
            } else {
                None
            };
            if num.is_none() {
                num = n;
            } else if num != n {
                num = None;
                break;
            }
        }
        if num.is_some() {
            results.push(*word);
        }
    }
    results
}

fn main() {
    for (inputs, mut outputs) in vec![
        (vec!["Hello", "Alaska", "Dad", "Peace"], vec!["Alaska", "Dad"])
    ] {
        let results = find_words(&inputs);
        assert_eq!(results.len(), outputs.len());
        outputs.sort();
        for word in results {
            assert_eq!(outputs.binary_search(&word).is_ok(), true);
            println!("Row(ok): {}", word);
        }
        println!("All OK!!!")
    }
}
