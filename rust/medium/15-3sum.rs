
use std::cmp::Ordering;

fn cmp_result(a: &Vec<i32>, b: &Vec<i32>) -> Ordering {
    match a[0].cmp(&b[0]) {
        Ordering::Equal => {
            match a[1].cmp(&b[1]) {
                Ordering::Equal => a[2].cmp(&b[2]),
                v @ _ => v
            }
        }
        v @ _ => v
    }
}

fn three_sum(nums: &Vec<i32>) -> Vec<Vec<i32>> {
    let mut results = Vec::new();
    let mut nums = nums.clone();
    nums.sort();
    for i in 0..(nums.len() - 2) {
        if i == 0 || (i > 0 && nums[i] != nums[i-1]) {
            let mut lo = i + 1;
            let mut hi = nums.len() - 1;
            let sum = 0 - nums[i];
            while lo < hi {
                if nums[lo] + nums[hi] == sum {
                    results.push(vec![nums[i], nums[lo], nums[hi]]);
                    while lo < hi && nums[hi] == nums[hi-1] { hi -= 1; }
                    while lo < hi && nums[lo] == nums[lo+1] { lo += 1; }
                    lo += 1;
                    hi -= 1;
                } else if nums[lo] + nums[hi] > sum { hi -= 1; }
                else { lo += 1 }
            }
        }
    }
    results
}

fn main() {
    for &(ref nums, ref results) in [
        (vec![-1, 0, 1, 2, -1, -4],
         vec![vec![-1, 0, 1], vec![-1, -1, 2]]),
        (
            vec![-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0],
            vec![vec![-5, 1, 4], vec![-4, 0, 4], vec![-4, 1, 3],
                 vec![-2, -2, 4], vec![-2, 1, 1], vec![0, 0, 0]]
        ),
        (
            vec![0, 0, 0, 0, 0],
            vec![vec![0, 0, 0]]
        )
    ].iter() {
        let mut nums = nums;
        let mut results = results.clone(); // TODO: Why need clone?
        results.sort_by(cmp_result);
        let mut rv = three_sum(&mut nums);
        rv.sort_by(cmp_result);
        println!("results={:?}, rv={:?}", results, rv);
        for (i, result) in rv.iter().enumerate() {
            for (j, n) in result.iter().enumerate() {
                assert_eq!(*n, results[i][j]);
            }
        }
    }
    println!("All tests DONE!")
}
