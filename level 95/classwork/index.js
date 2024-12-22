// 1) შექმენით ფუნქცია რომელსაც მატრიცა (2დ მასივი) 
// X-ების O-ების და ცარიელი სტრინგების. ფუნქციამ უნდა გამოთვალოს ფრეა, 
// თუ რომელამა მოთამაშემ მოიგო თამაში. ( ინფუთი ყოველთვის ვალიდური იქნება )


function checkGameResult(board) {
    const size = board.length;
    const isWinningLine = (line) => {
      if (line.every((cell) => cell === 'X')) return 'X';
      if (line.every((cell) => cell === 'O')) return 'O';
      return null;
    };

    for (let i = 0; i < size; i++) {
      const rowWinner = isWinningLine(board[i]);
      const columnWinner = isWinningLine(board.map((row) => row[i])); 
  
      if (rowWinner) return { winner: rowWinner, status: 'finished', result: `${rowWinner} won` };
      if (columnWinner) return { winner: columnWinner, status: 'finished', result: `${columnWinner} won` };
    }

    const mainDiagonal = board.map((row, i) => row[i]);
    const antiDiagonal = board.map((row, i) => row[size - 1 - i]);
  
    const mainDiagonalWinner = isWinningLine(mainDiagonal);
    const antiDiagonalWinner = isWinningLine(antiDiagonal);
  
    if (mainDiagonalWinner) return { winner: mainDiagonalWinner, status: 'finished', result: `${mainDiagonalWinner} won` };
    if (antiDiagonalWinner) return { winner: antiDiagonalWinner, status: 'finished', result: `${antiDiagonalWinner} won` };

    const isDraw = board.flat().every((cell) => cell === 'X' || cell === 'O');
    if (isDraw) return { winner: null, status: 'draw', result: 'Draw' };
  
    return { winner: null, status: 'ongoing', result: 'Game is still ongoing' };
}
  
const board1 = [
    ['X', 'O', 'X'],
    ['X', 'X', 'O'],
    ['O', 'O', 'X']
];
  
const board2 = [
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', '', '']
];
  
const board3 = [
    ['X', 'X', 'X'],
    ['O', 'O', ''],
    ['', '', '']
];
  
console.log(checkGameResult(board1));
console.log(checkGameResult(board2));
console.log(checkGameResult(board3));
  