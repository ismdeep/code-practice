#include "../library/header.hpp"
#include "../library/direction.hpp"

class JxustC2019BeginnerComeToRome {
public:
    void solve(std::istream &in, std::ostream &out) {
        int x1, y1, x2, y2;
        in >> x1 >> y1 >> x2 >> y2;
        int disx = x1 - x2;
        int disy = y1 - y2;
        bool found = false;
        TIMES(i,8) {
            if (dir_horse[i][0] == disx && dir_horse[i][1] == disy)
            {
                found = true;
            }
        }
        if (found) {
            out << "Yes" << endl;
        } else {
            out << "No" << endl;
        }
    }
};
