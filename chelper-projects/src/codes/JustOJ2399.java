package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class JustOJ2399 {
    public void solve(int testNumber, Scanner in, PrintWriter out) {
        int t;
        t = in.nextInt();
        while (t-- > 0) {
            int n = in.nextInt();
            int m = in.nextInt();
            int tmp;
            for (int i = 0; i < n; ++i) {
                tmp = in.nextInt();
            }
            if (n % (m + 1) != 0) {
                out.write("Ocean\n");
            }else{
                out.write("Starry\n");
            }
        }
    }
}
