package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class LeetCode_26_Remove_Duplicates_from_Sorted_Array {

    class Solution {
        public int removeDuplicates(int[] nums) {
            int len = 1;
            for (int i = 1; i < nums.length; i++) {
                if (nums[i] != nums[len - 1]) {
                    nums[len] = nums[i];
                    len++;
                }
            }
            return len;
        }
    }

    public void solve(int testNumber, Scanner in, PrintWriter out) {
        int[] nums = new int[]{0,0,1,1,1,2,2,3,3,4};
        int len = (new Solution()).removeDuplicates(nums);
        for (int i = 0; i < len; i++) {
            System.out.println((nums[i]));
        }
    }
}
