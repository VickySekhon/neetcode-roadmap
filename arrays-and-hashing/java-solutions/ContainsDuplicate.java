import java.util.HashSet;

public class ContainsDuplicate {
     public static void main(String[] args) {
          boolean testTrue = containsDup(new int[]{1,2,3,3,4});
          boolean testFalse = containsDup(new int[]{1,2,3,4,5});
          System.out.println("True test: " + testTrue);
          System.out.println("False test: "+ testFalse);
          return;
     }

     public static boolean containsDup(int[] nums) {
          HashSet<Integer> map = new HashSet<Integer>();

          for (int num : nums) {
               if (map.contains(num)) {
                    return true;
               }
               map.add(num);
          }

          return false;
     }
}
