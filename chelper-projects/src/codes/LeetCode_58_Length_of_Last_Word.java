package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class LeetCode_58_Length_of_Last_Word {

    class Solution {
        public int lengthOfLastWord(String s) {
            if (s == null) {
                return 0;
            }
            s = s.trim();
            if (s.equals("")) {
                return 0;
            }
            if (!s.contains(" ")) {
                return s.length();
            }
            return s.length() - s.lastIndexOf(" ") - 1;
        }
    }

    public void solve(int testNumber, Scanner in, PrintWriter out) {
        System.out.println((new Solution()).lengthOfLastWord("hello w"));
    }
}
