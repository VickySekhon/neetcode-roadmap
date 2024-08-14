import java.util.*;

public class ProductOfArrayExceptSelf {
     public static void main(String[] args) {
          System.out.println(productOfArrayExceptSelf(new int[] {1,2,3,4}));
          return;
     }


     public static List<Integer> productOfArrayExceptSelf(int[] arr) {
          List<Integer> prefix = new ArrayList<Integer>(arr.length);
          List<Integer> postfix = new ArrayList<Integer>(arr.length);

          // initialize lists
          postfix.add(1);
          prefix.add(1);

          for (int i = 1; i < arr.length; i++) {
               prefix.add(prefix.get(i-1) * arr[i-1]);
          }

          for (int i = arr.length-2; i > -1; i--) {
               postfix.add(0, postfix.get(0) * arr[i+1]);
          }

          int i = 0;
          List<Integer> result = new ArrayList<Integer>(arr.length);

          while (i < prefix.size()) {
               result.add(prefix.get(i)*postfix.get(i));
               i++;
          }

          return result;
     }
}
