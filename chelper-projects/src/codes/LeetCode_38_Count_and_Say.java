package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class LeetCode_38_Count_and_Say {

    class Solution {

        public String readOffStr(String str) {
            char ch = '-';
            int cnt = 0;
            String sentence = "";
            for (int i = 0; i < str.length(); i++) {
                if (ch != str.charAt(i)) {
                    if (cnt > 0) {
                        sentence = String.format("%s%d%c", sentence, cnt, ch);
                    }
                    cnt = 0;
                }
                cnt++;
                ch = str.charAt(i);
            }
            sentence = String.format("%s%d%c", sentence, cnt, ch);
            return sentence;
        }

        public String countAndSay(int n) {
            String initStr = "1";
            while (n-- > 1) {
                initStr = readOffStr(initStr);
            }
            return initStr;
        }
    }

    public void solve(int testNumber, Scanner in, PrintWriter out) {
        System.out.println((new Solution()).countAndSay(30));
    }
}
