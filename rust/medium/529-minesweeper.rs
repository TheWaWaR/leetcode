

fn click_it(board: &mut Vec<Vec<u8>>, x: usize, y: usize, mutate: bool) {
    let row_len = board.len();
    let col_len = board[0].len();
    match board[x][y] as char {
        'M' => {
            if mutate {
                board[x][y] = 'X' as u8;
            }
        },
        'E' => {
            let mut count = 0;
            let mut adjacents: Vec<(usize, usize)> = vec![];
            for i in [-1, 0, 1].iter() {
                let xi = x as i32 + i;
                if xi >= 0 && xi < row_len as i32 {
                    for j in [-1, 0, 1].iter() {
                        if *i == 0 && *j == 0 {
                            continue
                        }
                        let yj = y as i32 + j;
                        if yj >= 0 && yj < col_len as i32 {
                            let xi = xi as usize;
                            let yj = yj as usize;
                            adjacents.push((xi, yj));
                            if board[xi][yj] == 'M' as u8 {
                                count += 1;
                            }
                        }
                    }
                }
            }
            if count > 0 {
                board[x][y] = '0' as u8 + count;
            } else {
                board[x][y] = 'B' as u8;
                for (xi, yj) in adjacents {
                    click_it(board, xi, yj, false);
                }
            }
        },
        _ => {}
    }
}

fn update_board(board: &mut Vec<Vec<u8>>, click: (usize, usize)) {
    click_it(board, click.0, click.1, true);
}

fn main() {
    for &(ref cboard, click, ref result) in [
        (
            vec![
                vec!['E', 'E', 'E', 'E', 'E'],
                vec!['E', 'E', 'M', 'E', 'E'],
                vec!['E', 'E', 'E', 'E', 'E'],
                vec!['E', 'E', 'E', 'E', 'E']],
            (3, 0),
            vec![vec!['B', '1', 'E', '1', 'B'],
                 vec!['B', '1', 'M', '1', 'B'],
                 vec!['B', '1', '1', '1', 'B'],
                 vec!['B', 'B', 'B', 'B', 'B']]
        ),
        (
            vec![vec!['B', '1', 'E', '1', 'B'],
                 vec!['B', '1', 'M', '1', 'B'],
                 vec!['B', '1', '1', '1', 'B'],
                 vec!['B', 'B', 'B', 'B', 'B']],
            (1, 2),
            vec![vec!['B', '1', 'E', '1', 'B'],
                 vec!['B', '1', 'X', '1', 'B'],
                 vec!['B', '1', '1', '1', 'B'],
                 vec!['B', 'B', 'B', 'B', 'B']]
        ),
    ].iter() {
        let mut board = Vec::new();
        for crow in cboard {
            let mut row = Vec::new();
            for ccol in crow {
                row.push(*ccol as u8);
            }
            board.push(row);
        }
        println!("Board={:?}", board);
        println!("Click={:?}", click);
        println!("Result={:?}", result);
        update_board(&mut board, click);
        for x in 0..result.len() {
            for y in 0..result[0].len() {
                println!("Check: x={}, y={}", x, y);
                assert_eq!(board[x][y], result[x][y] as u8);
            }
        }
    }
    println!("All check done!");
}
