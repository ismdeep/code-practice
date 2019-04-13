package codes;

import java.math.BigInteger;
import java.util.Scanner;
import java.io.PrintWriter;

public class JustOJ2405 {

    static public long __gcd__ (long a, long b) {
        long tmp;
        while (b != 0) {
            tmp = a % b;
            a = b;
            b = tmp;
        }
        return a;
    }

    public void solve(int testNumber, Scanner in, PrintWriter out) {
        int n = in.nextInt();
        long val = Math.abs(in.nextLong());
        long tmp;
        for (int i = 1; i < n; ++i) {
            tmp = Math.abs(in.nextLong());
            val = __gcd__(val, tmp);
        }
        out.write(String.format("%d\n", val));
    }
}
