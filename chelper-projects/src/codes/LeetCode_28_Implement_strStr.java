package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class LeetCode_28_Implement_strStr {

    class Solution {
        public int strStr(String haystack, String needle) {
            if (needle.equals("")) {
                return 0;
            }
            return haystack.indexOf(needle);
        }
    }

    public void solve(int testNumber, Scanner in, PrintWriter out) {
        System.out.println((new Solution()).strStr("hello", "el"));
    }
}
