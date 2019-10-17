#include "../library/header.hpp"

int digital_count(int n) {
    if (n == 0) {
        return 1;
    }

    int cnt = 0;
    while (n) {
        ++cnt;
        n /= 10;
    }
    return cnt;
}



class DOTCPP1009 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    int n;
	    in >> n;
	    out << digital_count(n) << endl;
	    if (n == 0) {
	        out << "0" << endl << "0" << endl;
	        return;
	    }
	    int ans = 0;
	    stack<int> _stack;
	    while (n) {
	        _stack.push(n % 10);
	        ans *= 10;
	        ans += n % 10;
	        n /= 10;
	    }

	    bool flag = false;
	    while (!_stack.empty()) {
	        if (flag) {
	            out << " ";
	        }
	        flag = true;
	        out << _stack.top();
	        _stack.pop();
	    }
	    out << endl;

	    out << ans << endl;
	}
};
