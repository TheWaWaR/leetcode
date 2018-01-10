
fn three_sum_closest(nums: &Vec<i32>, target: i32) -> i32 {
    let mut nums = nums.clone();
    nums.sort();
    let mut min_sum = nums[0] + nums[1] + nums[2];
    let mut min_abs = (min_sum - target).abs();

    for i in 0..(nums.len() - 2) {
        let mut lo = i + 1;
        let mut hi = nums.len() - 1;
        while lo < hi {
            let sum = nums[i] + nums[lo] + nums[hi];
            if (sum - target).abs() < min_abs {
                min_sum = sum;
                min_abs = (sum - target).abs();
            }
            if sum > target {
                hi -= 1;
            } else if sum < target {
                lo += 1;
            } else {
                return target;
            }
        }
    }
    min_sum
}

fn main() {
    for &(ref nums, target, result) in [
        (vec![-1, 2, 1, -4], 1, 2),
        (vec![0, 0, 0], 3, 0),
        (vec![0, 0, 0, 0], 3, 0),
        (vec![-4, -4, -2, -1, 1], 2, -2)
    ].iter() {
        assert_eq!(three_sum_closest(nums, target), result);
        println!("Pass: nums={:?}, target={}, result={}", nums, target, result);
    }
    println!("All done!");
}
