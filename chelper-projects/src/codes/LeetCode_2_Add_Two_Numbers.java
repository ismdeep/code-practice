package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class LeetCode_2_Add_Two_Numbers {

    public class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }

        public ListNode parseListNode(String digitals) {
            if (digitals.length() <= 0) {
                return null;
            }
            return new ListNode( digitals.charAt(0) - '0', parseListNode(digitals.substring(1)));
        }

        @Override
        public String toString() {
            return String.format("%d %s", val, next != null ? next.toString() : "NULL");
        }
    }

    /**
     * Definition for singly-linked list.
     * public class ListNode {
     * int val;
     * ListNode next;
     * ListNode() {}
     * ListNode(int val) { this.val = val; }
     * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
     * }
     */
    class Solution {
        public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
            ListNode sum = new ListNode(0);
            ListNode cursorSum = sum;
            ListNode cursor1 = l1;
            ListNode cursor2 = l2;
            int remain = 0;
            while (cursor1 != null || cursor2 != null) {
                if (cursor1 != null) {
                    remain += cursor1.val;
                    cursor1 = cursor1.next;
                }
                if (cursor2 != null) {
                    remain += cursor2.val;
                    cursor2 = cursor2.next;
                }
                cursorSum.val = remain % 10;
                remain /= 10;
                if (remain > 0 || (cursor1 != null || cursor2 != null)) {
                    cursorSum.next = new ListNode(0);
                    cursorSum = cursorSum.next;
                }
            }
            while (remain > 0) {
                cursorSum.val = remain % 10;
                remain /= 10;
                if (remain > 0) {
                    cursorSum.next = new ListNode(0);
                }
            }
            return sum;
        }
    }

    public void solve(int testNumber, Scanner in, PrintWriter out) {
        ListNode a = new ListNode().parseListNode("5");
        ListNode b = new ListNode().parseListNode("5");

        System.out.println(a.toString());
        System.out.println(b.toString());

        ListNode sum = (new Solution()).addTwoNumbers(a, b);

        System.out.println(sum.toString());

    }
}
