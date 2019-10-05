/**
 * code generated by JHelper
 * More info: https://github.com/AlexeyDmitriev/JHelper
 * @author ismdeep
 */

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <stack>
#include <vector>
#include <algorithm>
#include <list>
#include <map>
#include <queue>
#include <bitset>
#include <numeric>
#include <sstream>
#include <limits>

using namespace std;


#define TIMES(id, size) for(int id = 0; id < (size); ++id)
#define FOR(type_id, id, from, to, step) for(type_id id = (from); id <= (to); id += step)
#define DBG(x) \
    (void)(cout << "L" << __LINE__ \
    << ": " << #x << " = " \
    << (x) << '\n')


typedef unsigned long long uint64_t;
typedef unsigned char uint8_t;


class Aizu0006 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    std::string str;
	    in >> str;
	    std::string ans;
	    for (int i = str.length() - 1; i >= 0; --i) {
	        ans += str[i];
	    }
	    out << ans << std::endl;
	}
};


int main() {
	Aizu0006 solver;
	std::istream& in(std::cin);
	std::ostream& out(std::cout);
	solver.solve(in, out);
	return 0;
}
