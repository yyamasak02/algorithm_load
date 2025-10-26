import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer n = sc.nextInt();
        Integer m = sc.nextInt();
        List<Integer> a = new ArrayList<>();
        while (sc.hasNext()) {
            a.add(sc.nextInt());
        }
        Integer difference = a.stream().collect(Collectors.summingInt(Integer::intValue)) - m;
        if (a.stream().anyMatch(v -> v.equals(difference))) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
