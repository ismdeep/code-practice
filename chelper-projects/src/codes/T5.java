package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class T5 {
    public void solve(int testNumber, Scanner in, PrintWriter out) {
        int year = in.nextInt();
        if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)) {
            out.write("yes");
        } else {
            out.write("no");
        }
    }
}
