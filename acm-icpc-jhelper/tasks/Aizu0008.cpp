#include <iostream>

class Aizu0008 {
public:
	void solve(std::istream& in, std::ostream& out) {
        int n;
        while (in >> n) {
            int cnt = 0;
            for (int i = 0; i < 10; ++i) {
                for (int j = 0; j < 10; ++j) {
                    for (int k = 0; k < 10; ++k) {
                        for (int l = 0; l < 10; ++l) {
                            if (i + j + k + l == n) {
                                ++cnt;
                            }
                        }
                    }
                }
            }
            out << cnt << std::endl;
        }
	}
};
