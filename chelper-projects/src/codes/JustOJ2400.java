package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class JustOJ2400 {
    public void solve(int testNumber, Scanner in, PrintWriter out) {
        while (in.hasNext()) {
            long val = in.nextLong();
            --val;
            if (val % 3 != 0) {
                out.write("-1 -1\n");
                continue;
            }

            val /= 3;
            long tmp = (long) Math.sqrt(val);
            if (tmp * (tmp + 1) != val) {
                out.write("-1 -1\n");
                continue;
            }

            out.write(String.format("%d %d\n", tmp, tmp + 1));
        }
    }
}
