import java.util.Scanner;
import java.util.stream.Stream;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.Comparator;
import java.util.LinkedHashMap;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        String s = sc.next();
        Map<String, Integer> map = IntStream.rangeClosed(0, n - k)
                .mapToObj(i -> s.substring(i, i + k))
                .collect(Collectors.toMap(str -> str, str -> 1, Integer::sum));
        // get max value
        Integer max = map.values().stream().max(Integer::compareTo).orElse(0);
        // filter map by max value
        map = map.entrySet().stream()
                .filter(entry -> entry.getValue().equals(max))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
        // sort map by key
        map = map.entrySet().stream()
                .sorted(Map.Entry.comparingByKey())
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue,
                        (e1, e2) -> e1, LinkedHashMap::new));
        String result = map.keySet().stream().collect(Collectors.joining(" "));
        System.out.println(max);
        System.out.println(result);
        return ;
    }
}
