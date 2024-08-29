import java.util.*;

public class ValidAnagram {
     public static void main(String[] args) {
          System.out.println(validAnagram("lleh", "hell"));
          return;
     }

     public static boolean validAnagram(String s, String v) {
          if (s.length() != v.length()) {
               return false;
          }

          // map a letter to it's frequency
          HashMap<Character, Integer> sMap = new HashMap<Character, Integer>();
          HashMap<Character, Integer> vMap = new HashMap<Character, Integer>();

          for (int i = 0; i < s.length(); i++) {

               char sChar = s.charAt(i);
               if (sMap.containsKey(sChar)) {
                    sMap.replace(sChar, sMap.get(sChar) + 1);
               } else {
                    sMap.put(sChar, 1);
               }
               char vChar = v.charAt(i);
               if (vMap.containsKey(vChar)) {
                    vMap.replace(vChar, vMap.get(vChar) + 1);
               } else {
                    vMap.put(vChar, 1);
               }
          }

          for (Map.Entry<Character, Integer> entry : sMap.entrySet()) {
               char sKey = entry.getKey();
               int sVal = entry.getValue();

               if (!vMap.containsKey(sKey)) {
                    return false;
               }

               if (sVal != vMap.get(sKey)) {
                    return false;
               }
          }

          return true;
     }
}
