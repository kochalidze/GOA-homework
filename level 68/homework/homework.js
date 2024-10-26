
//  1)
//  ```https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/javascript```
const booleanToString = b => b + "";

//  2)
//  ```https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/javascript```
const digitize = n =>
    [...String(n)].map(Number).reverse()

//  3)
//  ```https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/javascript```
function getGrade (s1, s2, s3) {
    const avg = (s1 + s2 + s3) / 3;
    if (avg >= 90) return 'A'
    if (avg >= 80) return 'B'
    if (avg >= 70) return 'C'
    if (avg >= 60) return 'C'
    return 'F'
}

//  4)
//  ```https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/javascript```
const areaOrPerimeter = function(l , w) {
    if (l === w) return l * w;
    return 2 * l + 2 * w;
};


//  ```7 Kyu```
//  1)
//  ```https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/javascript```
function dnaStrand(dna){
    let odject = {A:'T',  T:'A', C:'G', G:'C'}
    return dna.replace(/./g, e => object[e])
  }

//  2)
//  ```https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/javascript```
function reverseWords(str) {
    return str.split(' ').map(function(word){
      return word.split('').reverse().join('');
    }).join(' ');
  }

//  3)
// ```https://www.codewars.com/kata/546e2562b03326a88e000020/train/javascript```
const squareDigits = num =>
    +String(num).split('').map(e => (+e) ** 2).join('')

//  4)
//  ```https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/javascript```
//ვერ გავიგე