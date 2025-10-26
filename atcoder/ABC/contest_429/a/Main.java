import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer n = sc.nextInt();
        Integer m = sc.nextInt();
        IntStream.range(1, n+1).forEach(v -> {
            String res = "OK";
            if (v > m) {
                res = "Too Many Requests";
            }
            System.out.println(res);
        });
    }
}
