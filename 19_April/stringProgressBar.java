import java.util.ArrayList;
import java.util.Scanner;
import java.lang.System.*;

class stringProgressBar {

    public static ArrayList<Character> repeat(char character, int count) {
        ArrayList<Character> charList = new ArrayList<Character>();
        for (int i = 0; count > i; i++) {
            charList.add(character);
        }
        return charList;
    }

    public static void main(String[] args) {
        // System.out.print("Enter: ");
        // Scanner scan = new Scanner(System.in);
        // String alphabet = "abcdefghijklmnopqrstuvwxyz";
        // String word = scan.nextLine();
        // scan.close();

        // for (char ch : word.toCharArray()) {
        // int charInt = alphabet.indexOf(ch) + 1;
        // var list = repeat(ch, charInt);
        // for (char i : list) {
        // System.out.print(i);
        // }
        // }

        System.out.print("Enter: ");
        Scanner scan = new Scanner(System.in);
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String word = scan.nextLine();
        scan.close();
        int x = word.length();

        while (x > 0) {
            for (char ch : word.toCharArray()) {
                int charInt = alphabet.indexOf(ch) + 1;
                var list = repeat(ch, charInt);
                for (char i : list) {
                    System.out.print(i);
                }
                x--;
            }
        }
    }
}
