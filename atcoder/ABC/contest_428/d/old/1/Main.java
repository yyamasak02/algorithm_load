import static java.lang.Math.*;
import java.util.*;
import java.util.stream.*;

public class Main {

    static long ceilSqrt(long a) {
        if (a <= 0) return 0;
        long r = (long) sqrt(a - 1);
        return r + 1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        long[] pow = new long[20];
        pow[0] = 1;
        for (int i = 1; i < 20; i++) pow[i] = pow[i - 1] * 10;

        for (int t = 0; t < T; t++) {
            long C = sc.nextLong();
            long D = sc.nextLong();

            long smin = C + 1;
            long smax = C + D;
            int mLo = String.valueOf(smin).length();
            int mHi = String.valueOf(smax).length();

            long ans = IntStream.rangeClosed(mLo, mHi)
                .mapToLong(m -> {
                    long loM = pow[m - 1];
                    long hiM = pow[m] - 1;
                    long L = max(loM, smin);
                    long R = min(hiM, smax);
                    if (L > R) return 0L;

                    long a = C * pow[m] + L;
                    long b = C * pow[m] + R;
                    long sqrtB = (long) floor(sqrt(b));
                    long ceilA = ceilSqrt(a);

                    return max(0L, sqrtB - ceilA + 1);
                })
                .sum();

            System.out.println(ans);
        }
    }
}
