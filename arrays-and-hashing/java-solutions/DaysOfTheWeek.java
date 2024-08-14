import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class DaysOfTheWeek {
     public static void main(String[] args) {
          System.out.println(dayOfTheWeek("mon", 232));
          return;
     }

     public static String dayOfTheWeek(String startDay, int kDaysAfter) {
          List<String> days = new ArrayList<String>(Arrays.asList("mon", "tue", "wed", "thu", "fri", "sat", "sun"));

          int startIndx = days.indexOf(startDay);

          int endIndx = (startIndx + kDaysAfter) % 7;
          
          return days.get(endIndx);
     }

     
}
