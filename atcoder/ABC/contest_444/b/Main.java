import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer N = sc.nextInt();
        Integer K = sc.nextInt();
        Long result = IntStream.range(1, N + 1).filter(i -> {
            Integer tmp = 0;
            while (i != 0) {
                tmp += i % 10;
                i /= 10;
            }
            // System.out.println(tmp);
            return (tmp == K);
        })
        .count();
        System.out.println(result);
    }
}
