import java.util.Arrays;

/**
 * 3SumClosest
 */
public class ThreeSumClosest {
     public static void main(String[] args) {
          System.out.println(threeSumClosest(new int[]{1,3,3,5,6}, 5));
          return;
     }
     
     public static int threeSumClosest(int[] nums, int target) {
          int i = 0, j = 1, k = nums.length - 1;

          int result = nums[i]+nums[j]+nums[k];

          Arrays.sort(nums);

          for (i = 0; i < nums.length - 2; i++) {
               j = i+1; k = nums.length-1;
               while (j < k) {
                    int sum = nums[i]+nums[j]+nums[k];
                    if (sum > target) {
                         k--;
                    } else {
                         j++;
                    }
                    
                    result = Math.abs(target-sum) < Math.abs(target-result) ? sum : result;
               }
          }
          
          return result;
     }
}