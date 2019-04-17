import java.util.*;
import java.lang.System;

class Iteration {
    public static void main(String[] args) {
        Scanner obj1 = new Scanner(System.in);
        System.out.print("Enter Number: ");
        Integer num = obj1.nextInt();
        System.out.println("x: " + num);

        for (int i = num; num > 0; num--)
            if (i % num == 0) {
                System.out.println(num + " is a factor of " + i);
            } else if (num == 0) {
                break;
            } else {
                System.out.println(num + " is not factor of " + i);
            }

        // int i = num;
        // while (num > 0) {
        //     if (i % num == 0) {
        //         System.out.println(num + " is a factor of " + i);
        //         num--;
        //     } else if (num == 0) {
        //         break;
        //     } else {
        //         System.out.println(num + " is not factor of " + i);
        //         num--;
        //     }
        // }
    }

}
