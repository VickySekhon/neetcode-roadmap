

/*
     """
     Finds the length of the longest consecutive sequence in a given list of integers.

     Args:
          nums (List[int]): A list of integers.

     Returns:
          int: The length of the longest consecutive sequence.

     Example:
          >>> longest_consecutive_sequence([100, 4, 200, 1, 3, 2])
          4
     """
*/
function longestConsecutiveSequence(list: number[]): number {
     let max_seq_len = 0;

     for (let num of list) {
          if (!list.includes(num-1)) {
               let seq_length = 1;
               while (list.includes(num+seq_length)) {
                    seq_length++;
               }
               seq_length > max_seq_len ? max_seq_len = seq_length : max_seq_len;
          }
     }
     
     
     return max_seq_len;
}

console.log(longestConsecutiveSequence([100, 4, 200, 1, 3, 2]))