package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class ECUSTACM1256 {

    private static final long MOD = 1000000007;

    static class Matrix {
        public int n, m;
        public long[][] a;

        public Matrix(int __n__, int __m__) {
            this.n = __n__;
            this.m = __m__;
            a = new long[n][m];
        }

        public Matrix(int __n__, int __m__, int __init_val__) {
            this.n = __n__;
            this.m = __m__;
            a = new long[n][m];
            this.setAll(__init_val__);
        }

        public void setAll(int val) {
            for (int i = 0; i < this.n; i++) {
                for (int j = 0; j < this.m; j++) {
                    this.a[i][j] = val;
                }
            }
        }

        public void Show() {
            for (int i = 0; i < this.n; i++) {
                for (int j = 0; j < this.m; j++) {
                    System.out.print(String.format("%d ", this.a[i][j]));
                }
                System.out.println();
            }
        }

        public long sum() {
            long val = 0;
            for (int i = 0; i < this.n; i++) {
                for (int j = 0; j < this.m; j++) {
                    val += this.a[i][j];
                }
            }
            return val % MOD;
        }

        static public Matrix matrixMul(Matrix m1, Matrix m2) {
            Matrix matrix = new Matrix(m1.n, m2.m);
            for (int i = 0; i < m1.n; i++) {
                for (int j = 0; j < m2.m; j++) {
                    long ans = 0;
                    for (int k = 0; k < m1.m; k++) {
                        ans += m1.a[i][k] * m2.a[k][j];
                        ans %= MOD;
                    }
                    matrix.a[i][j] = ans % MOD;
                }
            }
            return matrix;
        }

        static public Matrix I(int n) {
            Matrix ans = new Matrix(n, n, 0);
            for (int i = 0; i < n; i++) {
                ans.a[i][i] = 1;
            }
            return ans;
        }

        static public Matrix matrixPow(Matrix matrix, int n) {
            if (n == 0) {
                return Matrix.I(matrix.n);
            }
            if (n == 1) {
                return matrix;
            }
            return matrixMul(
                    matrixPow(matrixPow(matrix, n / 2), 2),
                    matrixPow(matrix, n % 2)
            );
        }
    }


    public long pow(long a, long n) {
        if (n == 0) {
            return 1;
        }
        if (n == 1) {
            return a;
        }
        long v = pow(a, n / 2);
        v = v * v % MOD;
        if (n % 2 == 1) {
            v = v * a % MOD;
        }
        return v;
    }

    public void solve(int testNumber, Scanner in, PrintWriter out) {
        while (in.hasNext()) {
            Matrix M = new Matrix(6, 6, 1);
            Matrix A = new Matrix(6, 1, 1);
            int n;
            n = in.nextInt();
            int m;
            m = in.nextInt();
            for (int i = 0; i < m; i++) {
                int a, b;
                a = in.nextInt();
                b = in.nextInt();
                M.a[a - 1][b - 1] = 0;
                M.a[b - 1][a - 1] = 0;
            }
            long ans = Matrix.matrixMul(Matrix.matrixPow(M, n - 1), A).sum() * pow(4, n) % MOD;
            out.write(String.format("%d\n", ans));
        }
    }
}
