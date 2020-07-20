package codes;

import java.util.Scanner;
import java.io.PrintWriter;

public class LeetCode_83_Remove_Duplicates_from_Sorted_List {

    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }

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
     *     int val;
     *     ListNode next;
     *     ListNode() {}
     *     ListNode(int val) { this.val = val; }
     *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
     * }
     */
    class Solution {
        public ListNode deleteDuplicates(ListNode head) {
            if (head == null) {
                return head;
            }
            ListNode current = head;
            ListNode cursor = head.next;
            while (cursor != null) {
                if (cursor.val != current.val) {
                    current = cursor;
                    cursor = cursor.next;
                } else {
                    cursor = cursor.next;
                    current.next = cursor;
                }
            }
            return head;
        }
    }

    public void solve(int testNumber, Scanner in, PrintWriter out) {
        ListNode listNode = new ListNode().parseListNode("");
        System.out.println((new Solution()).deleteDuplicates(listNode));
    }
}
