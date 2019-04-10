package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class JustOJ1970 {

    private static String encrypt(String str) {
        String keypad = "22233344455566677778889999";
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < str.length(); ++i) {
            if (str.charAt(i) >= 'A' && str.charAt(i) <= 'Z') {
                if ('Z' == str.charAt(i)) ans.append('a');
                else ans.append((char) (str.charAt(i) + 33));
            }else if (str.charAt(i) >= 'a' && str.charAt(i) <= 'z'){
                ans.append(keypad.charAt(str.charAt(i) - 'a'));
            }else {
                ans.append(str.charAt(i));
            }
        }
        return ans.toString();
    }

    public void solve(int testNumber, Scanner in, PrintWriter out) {
        while (in.hasNext()) {
            String s = in.nextLine();
            out.write(encrypt(s));
            out.write("\n");
        }
    }
}
