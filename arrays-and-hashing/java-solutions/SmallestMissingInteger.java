import java.util.HashSet;
import java.util.Set;

public class SmallestMissingInteger {
     public static void main(String[] args) {
          System.out.println(smallestMissing(new int[] { 1, 2, 3, 4, 5 }));
          return;
     }

     private static int smallestMissing(int[] arr) {
          HashSet<Integer> unique = new HashSet<Integer>();

          for (int num : arr) {
               unique.add(num);
          }

          int smallest = 1;
          while (unique.contains(smallest)) {
               smallest++;
          }
          return smallest;
     }
}