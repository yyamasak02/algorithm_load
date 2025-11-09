import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Integer a = sc.nextInt();
        Integer b = sc.nextInt();
        Integer c = sc.nextInt();
        Integer d = sc.nextInt();

        String result = "";
        if ((a <= c) && (b <= d)){
            result = "No";
        }
        else if (a <= c){
            result = "Yes";
        }
        else {
            result = "No";
        }
        System.out.println(result);
    }
}
