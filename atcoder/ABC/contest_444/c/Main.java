import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer N = sc.nextInt();
        List<Integer> A = new ArrayList<>();
        for (int i=0;i<N;++i){
            A.add(sc.nextInt());
        }
        List<Integer> sortedA = A.stream()
            .sorted(Comparator.naturalOrder())
            .collect(Collectors.toList());
        System.out.println(sortedA);
    }
}
