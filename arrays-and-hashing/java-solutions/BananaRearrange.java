import java.util.HashMap;
import java.util.Map;

/**
 * BananaRearrange
 */
public class BananaRearrange {

     public static void main(String[] args) {
          System.out.println(bananaRearrange("jlfsadjklfsadbjnan"));
          return;
     }

     public static int bananaRearrange(String letters) {
          String charsInBananna = "ban";

          HashMap<Character, Integer> map = new HashMap<Character, Integer>();

          for (char letter : letters.toCharArray()) {
               if (charsInBananna.indexOf(letter) != -1) {
                    if (map.containsKey(letter)) {
                         map.put(letter, map.get(letter)+1);
                    } else {
                         map.put(letter, 1);
                    }
               }
          }
          int ways = 0;
          while (map.get('a') == 3 && map.get('b') == 1 && map.get('n') == 2) {
               ways++;
               map.put('a', map.get('a')-3);
               map.put('b', map.get('b')-1);
               map.put('n', map.get('n')-2);
          }
          return ways;
     }
}