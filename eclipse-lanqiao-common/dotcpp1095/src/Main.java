import java.util.Scanner;

public class Main {
	
	public static int cnt(int val) {
		int cnt_val = 1;
		while (val != 1) {
			if (val % 2 == 0) {
				val /= 2;
			} else {
				val = val * 3 + 1;
			}
			++cnt_val;
		}
		return cnt_val;
	}
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		while (in.hasNext()) {
			int left, right;
			left = in.nextInt();
			right = in.nextInt();
			
			int a = left;
			int b = right;
			
			if (left > right) {
				int t = left; left = right; right = t;
			}
			int max_step = cnt(left);
			for (int val = left + 1; val <= right; val++) {
				int tmp_step = cnt(val);
				if (tmp_step > max_step) {
					max_step = tmp_step;
				}
			}
			System.out.println(a + " " + b + " " + max_step);
		}
		in.close();
	}
}
