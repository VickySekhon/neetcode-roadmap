import java.util.*;

public class GroupAnagrams {
     public static void main(String[] args) {
          System.out.println(groupedAnagrams(new String[]{"eat","tea","tan","ate","nat","bat"}));
          return;
     }

     public static List<List<String>> groupedAnagrams(String[] strs) {
          
          HashMap<String, ArrayList<String>> anagrams = new HashMap<String, ArrayList<String>>();

          for (String word : Arrays.asList(strs)) {
               char[] key = word.toCharArray();
               Arrays.sort(key);
               

               if (anagrams.containsKey(new String(key))) {
                    anagrams.get(new String(key)).add(word);
               } else {
                    anagrams.put(new String(key), new ArrayList<String>(Arrays.asList(word)));
               }
          }

          List<List<String>> grouped = new ArrayList<List<String>>();

          for (ArrayList<String> group : anagrams.values()) {
               grouped.add(group);
          }

          return grouped;
     }
}
