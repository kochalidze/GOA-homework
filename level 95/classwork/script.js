// 2) შექმენით ფუნქცია რომელსაც მატრიცა (2დ მასივი) X-ების O-ების და ცარიელი
//  სტრინგების. ფუნქციამ უნდა დაადგინოს რომელი მოთამაშე მოიგებდა
//   "Connrect 4'-ის თამაშში, სიმარტივითვის თქვენ არ გიწევთ დიაგონალურად 
//   შემოწმება. ( თუ თამაში არ იცით რესურსებში აღწერას ჩავაგდებ ) ( სირთულე 8/10 ) 

function checkConnect4(board) {
    const rows = board.length;
    const cols = board[0].length;
    const checkLine = (line) => {
      let count = 1;
      for (let i = 1; i < line.length; i++) {
        if (line[i] === line[i - 1] && line[i] !== '') {
          count++;
          if (count === 4) return line[i];
        } else {
          count = 1;
        }
      }
      return null;
    };
 
    for (let row of board) {
      const winner = checkLine(row);
      if (winner) return `${winner} won!`;
    }

    for (let col = 0; col < cols; col++) {
      const column = board.map((row) => row[col]);
      const winner = checkLine(column);
      if (winner) return `${winner} won!`;
    }
  

    return "No winner!";
}

const board1 = [
    ['X', 'X', 'X', 'X', '', '', ''],
    ['O', 'O', '', '', '', '', ''],
    ['O', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '']
];
  
const board2 = [
    ['X', 'O', 'X', '', '', '', ''],
    ['O', 'O', 'X', '', '', '', ''],
    ['X', 'O', 'X', '', '', '', ''],
    ['O', 'O', 'O', 'O', '', '', '']
];
  
const board3 = [
    ['X', 'O', 'X', '', '', '', ''],
    ['O', 'X', 'X', '', '', '', ''],
    ['X', 'O', 'O', '', '', '', ''],
    ['O', 'X', 'O', '', '', '', '']
];
  
console.log(checkConnect4(board1));
console.log(checkConnect4(board2));
console.log(checkConnect4(board3));
  