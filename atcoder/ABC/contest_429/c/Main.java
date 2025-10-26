import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Long n = Long.parseLong(sc.next());
        Map<Long, Long> a = new HashMap<>();
        while (sc.hasNextLong()) {
            a.merge(Long.parseLong(sc.next()), Long.valueOf(1), (oldValue, newValue) -> oldValue + newValue);
        }
        Long ans = a.values().stream()
            .filter(v -> v >= 2)
            .mapToLong(v -> v * (v - 1) * (n - v) / 2)
            .sum();
        System.out.println(ans);
    }
}
