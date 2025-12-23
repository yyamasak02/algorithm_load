import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int s = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();
        int x = sc.nextInt();
        int c = x / (a + b);
        int ans = s * a * c + Math.min(x % (a + b), a) * s;
        System.out.println(ans);
    }
}
