import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double ans = 0;
        Pair p = new Pair(0, 0, 0, 0);
        Integer n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            double x = sc.nextInt();
            double y = sc.nextInt();
            p.swap(x, y);
            ans += p.calcDistance();
        }
        p.swap(0, 0);
        ans += p.calcDistance();
        System.out.println(ans);
    }
}

class Pair {
    public double a;
    public double b;
    public double c;
    public double d;

    Pair(double a, double b, double c, double d) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.d = d;
    }
    public double calcDistance() {
        double distance = Math.pow((this.a - this.c), 2) + Math.pow((this.b - this.d), 2);
        return Math.sqrt(distance);
    }

    public void swap(double x, double y) {
        this.a = c;
        this.b = d;
        this.c = x;
        this.d = y;
    }
}
