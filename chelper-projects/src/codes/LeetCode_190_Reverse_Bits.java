package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class LeetCode_190_Reverse_Bits {
    public class Solution {
        // you need treat n as an unsigned value
        public int reverseBits(int n) {
            return Integer.reverse(n);
        }
    }

    public void solve(int testNumber, Scanner in, PrintWriter out) {
        System.out.println((new Solution()).reverseBits(43261596));
    }
}
