package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class HDU2268 {
    public void solve(int testNumber, Scanner in, PrintWriter out) {
        while (in.hasNext()) {
            int a, b, c;
            a = in.nextInt();
            b = in.nextInt();
            c = in.nextInt();
            double t;
            double s1;
            if (b > a) {
                s1 = ((b + a) * 1.0 / (b + 3 * a)) * c;
                t = s1 / b + (c - s1) / a;
            } else {
                t = c * 1.0 / a;
            }
            out.write(String.format("%.3f\n", t));
        }
    }
}
