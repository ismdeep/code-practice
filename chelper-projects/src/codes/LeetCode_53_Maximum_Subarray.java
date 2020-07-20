package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class LeetCode_53_Maximum_Subarray {

    class Solution {
        public int maxSubArray(int[] nums) {
            int val = 0;
            int maxVal = Integer.MIN_VALUE;
            for (int num : nums) {
                if (val >= 0) {
                    val += num;
                } else {
                    val = num;
                }
                if (val > maxVal) {
                    maxVal = val;
                }
            }
            return maxVal;
        }
    }

    public void solve(int testNumber, Scanner in, PrintWriter out) {
        int[] nums = new int[]{-2, 1};
        System.out.println((new Solution()).maxSubArray(nums));
    }
}
