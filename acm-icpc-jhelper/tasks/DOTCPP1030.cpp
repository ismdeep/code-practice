#include "../library/header.hpp"

class DOTCPP1030 {
public:
    void solve(std::istream &in, std::ostream &out) {
        int a[3][3];
        TIMES(i, 3) {
	        TIMES(j, 3) {
	            in >> a[i][j];
	        }
        }
        TIMES(i, 3) {
            TIMES(j, 3) {
                out << a[j][i] << " ";
            }
            out << endl;
        }
    }
};
