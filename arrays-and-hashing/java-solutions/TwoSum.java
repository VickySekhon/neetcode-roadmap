import java.util.*;

public class TwoSum {
     public static void main(String[] args) {
          int[] indices = twoSum(new int[]{1,2,3,4}, 5);
          for (int index : indices) {
               System.out.println(index);
          }
          return;
     }

     public static int[] twoSum(int[] nums, int target) {
          HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
          
          for (int i = 0; i < nums.length; i++) {
               int valWeNeed = target - nums[i];
               if (map.containsKey(valWeNeed)) {
                    return new int[]{map.get(valWeNeed), i};
               }
               map.put(nums[i], i);
          }
          return new int[]{0};
     }
}
