import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String strN = sc.next();
        String result = (strN.charAt(0) == strN.charAt(1) && strN.charAt(1) == strN.charAt(2)) ? "Yes" : "No";
        System.out.println(result);
    }
}
