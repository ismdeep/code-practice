package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class ECUSTACM1252 {
    public void solve(int testNumber, Scanner in, PrintWriter out) {
        int n = 1;
        boolean found = false;
        while (!found) {
            String ans = String.format("%d%d", n * n, n * n * n);
            if (ans.length() == 10
                    && ans.contains("0")
                    && ans.contains("1")
                    && ans.contains("2")
                    && ans.contains("3")
                    && ans.contains("4")
                    && ans.contains("5")
                    && ans.contains("6")
                    && ans.contains("7")
                    && ans.contains("8")
                    && ans.contains("9")
            ) {
                found = true;
                out.write(String.format("%d\n", n));
            }
            ++n;
        }
    }
}
