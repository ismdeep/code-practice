package codes;

import java.util.HashMap;
import java.util.Scanner;
import java.io.PrintWriter;

public class LeetCode_1_Two_Sum {

    class Solution {
        public int[] twoSum(int[] nums, int target) {
            int[] result = new int[2];
            HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
            for (int i = 0; i < nums.length; i++) {
                if (hashMap.containsKey(target - nums[i])) {
                    result[0] = hashMap.get(target - nums[i]);
                    result[1] = i;
                    return result;
                }
                hashMap.put(nums[i], i);
            }

            return result;
        }
    }

    public void solve(int testNumber, Scanner in, PrintWriter out) {
        int[] nums = new int[]{2, 7, 11, 15};
        int target = 9;
        int[] a = (new Solution()).twoSum(nums, target);
        assert target==nums[a[0]] + nums[a[1]];
        System.out.println("OK!");
    }
}
