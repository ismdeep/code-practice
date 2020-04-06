package codes;

import java.math.BigInteger;
import java.util.Scanner;
import java.io.PrintWriter;

public class T71 {
    public void solve(int testNumber, Scanner in, PrintWriter out) {
        int n;
        n = in.nextInt();
        BigInteger ans = new BigInteger("1");
        for (int i = 1; i <= n; i++) {
            ans = ans.multiply(new BigInteger(Integer.toString(i)));
        }
        out.write(ans.toString());
    }
}
