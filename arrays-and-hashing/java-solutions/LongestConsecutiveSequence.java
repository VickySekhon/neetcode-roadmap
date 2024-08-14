import java.util.*;

public class LongestConsecutiveSequence {
     public static void main(String[] args) {
          System.out.println(longestConsecutiveSequence(new int[]{9,1,4,7,3,-1,0,5,8,-1,6}));
          return;
     }

     public static int longestConsecutiveSequence(int[] nums) {
          int maxSeqLen = 0;

          Set<Integer> uniqueNums = new HashSet<Integer>();
          for (int num : nums) {
               uniqueNums.add(num);
          }

          for (int uniqueNum : uniqueNums) {
               // start of a new sequence
               if (!uniqueNums.contains(uniqueNum-1)) {
                    int currentSeqLen = 0;
                    while (uniqueNums.contains(currentSeqLen+uniqueNum)) {
                         currentSeqLen++;
                    }
                    maxSeqLen = Math.max(currentSeqLen, maxSeqLen);
               }
          }
          
          return maxSeqLen;
     }
}
