import java.util.Scanner;
import java.util.stream.IntStream;


class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer N = sc.nextInt();
        String S = sc.next();
        System.out.println(
            IntStream.range(0, N - 2)
                .filter(i -> {
                    String sub = S.substring(i, i + 3);
                    return sub.equals("#.#");
                })
                .count()
        );
    }
}
