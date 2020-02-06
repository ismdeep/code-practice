package codes;

import java.util.HashSet;
import java.util.Scanner;
import java.io.PrintWriter;

public class ECUSTACM1254 {

    static HashSet<String> hashSet = new HashSet<String>();
    static int count = 0;

    static char []cur = new char[12];
    static int count1 = 3;
    static int count2 = 4;
    static int count3 = 5;

    static void dfs(int index) {
        if (index == 12) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 12; i++) {
                sb.append(cur[i]);
            }
            push(sb.toString());
            return;
        }

        if (count1 > 0) {
            cur[index] = '1';
            --count1;
            dfs(index + 1);
            ++count1;
        }
        if (count2 > 0) {
            cur[index] = '2';
            --count2;
            dfs(index + 1);
            ++count2;
        }
        if (count3 > 0) {
            cur[index] = '3';
            --count3;
            dfs(index + 1);
            ++count3;
        }
    }

    static String shift(String str) {
        return str.substring(1) + str.substring(0, 1);
    }

    static String rotate(String str) {
        StringBuilder sb = new StringBuilder();
        for (int i = str.length() - 1; i >= 0; i--) {
            sb.append(str.charAt(i));
        }
        return sb.toString();
    }

    static void push(String str) {
        if (!hashSet.contains(str)) {
            ++count;
        }
        String tmp = str;
        for (int i = 0; i < 12; i++) {
            hashSet.add(tmp);
            tmp = shift(tmp);
        }

        tmp = rotate(str);
        for (int i = 0; i < 12; i++) {
            hashSet.add(tmp);
            tmp = shift(tmp);
        }
    }


    public void solve(int testNumber, Scanner in, PrintWriter out) {
        dfs(0);
        out.write(String.format("%d\n", count));
    }
}
