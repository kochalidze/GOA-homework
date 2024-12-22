// 5) შევქმნათ ფუნქცია რომელიც დააბრუნებს პირველ
//  არა-განმეორებად ასოს რომელიც შეხვდება. ( სირთულე 4/10 )

function firstNonRepeatingChar(str) {
    const charCount = {};

    for (let char of str) {
      charCount[char] = (charCount[char] || 0) + 1;
    }

    for (let char of str) {
      if (charCount[char] === 1) {
        return char;
      }
    }
  
    return null;
  }

  console.log(firstNonRepeatingChar("swiss")); // "w"
  console.log(firstNonRepeatingChar("hello")); // "h"
  console.log(firstNonRepeatingChar("aabbcc")); // null
  console.log(firstNonRepeatingChar("xxyyzzq")); // "q"
  