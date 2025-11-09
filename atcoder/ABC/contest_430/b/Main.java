
// 全通り取り出す。その際に１行に並べることで集合として扱うことができる。

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Integer n = sc.nextInt();
        Integer m = sc.nextInt();
        List<String> a = new ArrayList<>();
        Set<String> b = new HashSet<>();
        for (int i = 0; i < n; i++) {
            a.add(sc.next());
        }
        // for (int i = 0; i <= n - m; i++) {
        //     for (int j = 0; j <= n - m; j++) {
        //         StringBuilder s = new StringBuilder();
        //         for (int k = i; k < i + m; k++) {
        //             s.append(a.get(k).substring(j, j+m));
        //         }
        //         b.add(s.toString());
        //     }
        // }

        long result = IntStream.rangeClosed(0, n - m)
            .boxed()
            .flatMap(i ->
                IntStream.rangeClosed(0, n - m)
                    .mapToObj(j -> {
                        StringBuilder s = new StringBuilder();
                        for (int k = i; k < i + m; k++) {
                            s.append(a.get(k).substring(j, j + m));
                        }
                        return s.toString();
                    })
            )
            .distinct()
            .count();
        System.out.println(result);
    }
}
