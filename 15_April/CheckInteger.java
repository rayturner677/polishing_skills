import java.util.*;
import java.lang.System;

class CheckInteger {
    public static void main(String[] args) {
        Scanner obj1 = new Scanner(System.in);

        System.out.println("Insert positive number: ");
        Integer num = obj1.nextInt();
        // for (int i = obj1.nextInt(); i >= 0; i--) {
        // if (i % 2 == 0) {
        // System.out.println(i + " is even!");
        // } else {
        // System.out.println(i + " is odd!");
        // }
        // }

        while (num > 0) {
            if (num % 2 == 0) {
                System.out.println(num + " is even!");
            } else {
                System.out.println(num + " is odd!");
            }
            num -= 1;
        }
    }

}
