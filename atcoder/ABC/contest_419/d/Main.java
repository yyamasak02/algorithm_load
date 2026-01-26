import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer N = sc.nextInt();
        Integer M = sc.nextInt();
        String S = sc.next();
        String T = sc.next();
        List<Integer> transferCount = new ArrayList<>(Collections.nCopies(N + 1, 0));
        IntStream.range(0, M).forEach(i -> {
            Integer Li = sc.nextInt();
            Integer Ri = sc.nextInt();
            Li--;
            Ri--;
            transferCount.set(Li, transferCount.get(Li) + 1);
            transferCount.set(Ri + 1, transferCount.get(Ri + 1) - 1);
        });
        Integer[] array = transferCount.toArray(new Integer[0]);
        Arrays.parallelPrefix(array, (a, b) -> a + b);
        StringBuilder result = new StringBuilder();
        IntStream.range(0, N).forEach(index -> {
            if (array[index] % 2 == 0) {
                result.append(S.charAt(index));
            }
            else {
                result.append(T.charAt(index));
            }
        });
        System.out.println(result.toString());
    }
}
