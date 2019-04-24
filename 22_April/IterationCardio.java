import java.util.ArrayList;
import java.util.Scanner;

class IterationCardio {
    public static void main(String[] args) {

        ArrayList<Integer> components = new ArrayList<Integer>();
        components.add(456);
        components.add(254);
        components.add(25);
        components.add(26234);

        findDifference(components);
        findDifferenceWhile(components);
    }

    public static void findDifference(ArrayList<Integer> list_a) {
        int high = list_a.get(0);
        int low = list_a.get(0);

        for (int item : list_a) {
            if (high < item) {
                high = item;
            } else if (low > item) {
                low = item;
            }
        }
        System.out.println(high - low);
    }

    public static void findDifferenceWhile(ArrayList<Integer> list) {
        int high = list.get(0);
        int low = list.get(0);

        int i = 0;
        while (i < list.size()) {
            if (high < list.get(i)) {
                high = list.get(i);
            } else if (low > list.get(i)) {
                low = list.get(i);
            }
            i++;
        }
        System.out.println(high - low);
    }
}
