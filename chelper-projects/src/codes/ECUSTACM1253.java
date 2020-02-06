package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class ECUSTACM1253 {

    static long C(long n, long k) {
        long ans = 1;
        for (long i = 0; i < k; i++) {
            ans *= (n - i);
        }
        for (long i = 1; i <= k; i++) {
            ans /= i;
        }
        return ans;
    }

    public void solve(int testNumber, Scanner in, PrintWriter out) {
        long ans = 0;
        for (long count4 = 3; count4 >= 0; count4--) {
            for (long count3 = 4; count3 >= 0; count3--) {
                for (long count2 = 6; count2 >= 0; count2--) {
                    for (long count1 = 13; count1 >= 0; count1--) {
                        if (count4 * 4 + count3 * 3 + count2 * 2 + count1 * 1 == 13) {
                            long tmp = C(13, count4) * C(13 - count4, count3) * C(13 - count4 - count3, count2) * C(13 - count4 - count3 - count2, count1);
                            ans += tmp;
                        }
                    }
                }
            }
        }
        out.write(String.format("%d\n", ans));
    }
}
