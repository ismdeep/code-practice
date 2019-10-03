#include "../library/header.hpp"

class Aizu0013 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    stack<int> _stack;
	    int n, val;
	    while (in >> n) {
	        if (0 == n) {
	            out << _stack.top() << endl;
	            _stack.pop();
	        } else {
	            _stack.push(n);
	        }
	    }
	}
};
