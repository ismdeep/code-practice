package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class HDU2687 {

    public static int[][] rotate(int a[][], int n) {
        int[][] b = new int[n][n];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                b[n-j-1][i] = a[i][j];
            }
        }
        return b;
    }

    public void solve(int testNumber, Scanner in, PrintWriter out) {
        while (in.hasNext()) {
            int n = in.nextInt();
            int [][]a = new int[n][n];
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    a[i][j] = in.nextInt();
                }
            }
            int k = in.nextInt();

            int[][] b0 = a;
            int[][] b1 = rotate(rotate(rotate(b0, n),n),n);
            int[][] b2 = rotate(rotate(rotate(b1, n),n),n);
            int[][] b3 = rotate(rotate(rotate(b2, n),n),n);

            long [][]ans = new long[n][n];

            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    ans[i][j] = b0[i][j] + b1[i][j] + b2[i][j] + b3[i][j];
                    ans[i][j] *= ((k + 1) / 4);
                }
            }

            if ((k + 1) % 4 == 1) {
                for (int i = 0; i < n; ++i) {
                    for (int j = 0; j < n; ++j) {
                        ans[i][j] += b0[i][j];
                    }
                }
            }
            if ((k + 1) % 4 == 2) {
                for (int i = 0; i < n; ++i) {
                    for (int j = 0; j < n; ++j) {
                        ans[i][j] += b0[i][j] + b1[i][j];
                    }
                }
            }
            if ((k + 1) % 4 == 3) {
                for (int i = 0; i < n; ++i) {
                    for (int j = 0; j < n; ++j) {
                        ans[i][j] += b0[i][j] + b1[i][j] + b2[i][j];
                    }
                }
            }


            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (j != 0) {
                        out.write(" ");
                    }
                    out.write(Long.toString(ans[i][j]));
                }
                out.write("\n\n");
            }
        }
    }
}
