package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class ECUSTACM1255 {
    public void solve(int testNumber, Scanner in, PrintWriter out) {
        int n;
        while (in.hasNext()) {
            n = in.nextInt();
            int count = 0;
            count = n;
            while (n >= 3) {
                count += (n / 3);
                n = n - 3 * (n / 3) + (n / 3);
            }
            out.write(String.format("%d\n", count));
        }
    }
}
