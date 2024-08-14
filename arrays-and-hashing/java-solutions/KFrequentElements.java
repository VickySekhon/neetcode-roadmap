import java.util.*;

public class KFrequentElements {
     public static void main(String[] args) {
          System.out.println(kFrequentElements(new int[] { 1, 2, 2, 3, 3, 3 }, 2));
          return;
     }

     public static List<Integer> kFrequentElements(int[] elements, int k) {
          // stores numbers and their frequencies
          HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

          // used to index a number by it's frequency
          List<List<Integer>> arr = new ArrayList<List<Integer>>();
          // initialize the array
          for (int i = 0; i < elements.length; i++) {
               arr.add(new ArrayList<>(Arrays.asList()));
          }

          // populate the map
          for (int element : elements) {
               if (map.containsKey(element)) {
                    map.put(element, map.get(element) + 1);
               } else {
                    map.put(element, 1);
               }
          }

          // populate the array from the map
          for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
               int key = entry.getKey();
               int frequencyIndx = entry.getValue();

               arr.get(frequencyIndx).add(key);
          }

          // final result
          List<Integer> result = new ArrayList<Integer>();

          // find the 'k' most frequent elements in the array
          for (int i = arr.size() - 1; i > -1; i--) {
               List<Integer> subArr = arr.get(i);
               for (int j = 0; j < subArr.size(); j++) {
                    if (result.size() != k) {
                         result.add(subArr.get(j));
                    }
               }
          }
          return result;
     }
}
