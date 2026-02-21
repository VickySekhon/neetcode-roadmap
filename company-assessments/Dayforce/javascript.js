// 1. Write a function that reverses a string (without using any built in JS helper functions).

function reverseString(str) {
  let reversedString = "";

  for (let i = str.length - 1; i >= 0; i--) {
    reversedString += str[i];
  }

  return reversedString;
}
//console.log(reverseString("hello")) // Should print "olleh"

// 2. Write a function to reverse the order of words in a sentence using as little code as possible. Feel free to use built in JS helper functions.
// You can assume that str does not begin or end with a space.

function reverseSentence(str) {
  // let words = str.split(" ");

  // let reversedWords = words.reverse();
  return str.split(" ").reverse().join(" ");
}
//console.log(reverseSentence("the sky is blue")) // Should print "blue is sky the"

// 3. BONUS Rewrite reverseString to use recursion
function reverseString(str) {
  /* base case:
           hello
            |  | 
           hel lo
           |     |
          h el  l o
            |
           e l
   
       length = 1
       */

  if (str.length === 1) {
    return str;
  }

  // divide
  let midpoint = Math.floor(str.length / 2);

  let h1 = str.substring(0, midpoint);
  let h2 = str.substring(midpoint);

  let str1 = reverseString(h1);
  let str2 = reverseString(h2);

  // reverse
  return str2 + str1;
}

console.log(reverseString("hello"));
