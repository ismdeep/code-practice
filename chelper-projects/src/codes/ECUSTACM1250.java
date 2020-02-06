package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class ECUSTACM1250 {
    public void solve(int testNumber, Scanner in, PrintWriter out) {
        while (in.hasNext()) {
            int n = in.nextInt();
            boolean found = false;
            for (int a = 1; a * a <= n; a++) {
                for (int b = a; a * a + b * b <= n; b++) {
                    for (int c = b; a * a + b * b + c * c <= n; c++) {
                        if (a * a + b * b + c * c == n) {
                            found = true;
                            out.write(String.format("%d %d %d\n", a, b, c));
                        }
                    }
                }
            }
            if (!found) {
                out.write("No Solution\n");
            }
        }
        in.close();
    }
}
