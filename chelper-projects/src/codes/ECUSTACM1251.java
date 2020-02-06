package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class ECUSTACM1251 {

    static int[] monthDayCount = {
            0,
            31,
            28,
            31,
            30,
            31,
            30,
            31,
            31,
            30,
            31,
            30,
            31
    };

    static int[] monthLeapDayCount = {
            0,
            31,
            29,
            31,
            30,
            31,
            30,
            31,
            31,
            30,
            31,
            30,
            31
    };

    static boolean isLeapYear(int year) {
        return year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);
    }

    public void solve(int testNumber, Scanner in, PrintWriter out) {
        while (in.hasNext()) {
            int year, month, day, dayCount;
            year = in.nextInt();
            month = in.nextInt();
            day = in.nextInt();
            dayCount = in.nextInt();
            while (dayCount-- > 0) {
                ++day;
                if (isLeapYear(year)) {
                    if (day > monthLeapDayCount[month]) {
                        month++;
                        day = 1;
                    }
                } else {
                    if (day > monthDayCount[month]) {
                        month++;
                        day = 1;
                    }
                }
                if (month == 13) {
                    month = 1;
                    year++;
                }
            }
            out.write(String.format("%04d-%02d-%02d\n", year, month, day));
        }
    }
}
