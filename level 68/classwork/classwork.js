// 1) https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/javascript
function findAverage(array) {
    if (array.length === 0) return 0;
    const sum = array.reduce((sum, n) => {
      return sum + n;
    }, 0)
    return sum / array.length;
  }
  
// 2) https://www.codewars.com/kata/53dc23c68a0c93699800041d/train/javascript
// 3) https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/javascript
// 4) https://www.codewars.com/kata/5556282156230d0e5e000089/train/javascript
// 5) https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/javascript