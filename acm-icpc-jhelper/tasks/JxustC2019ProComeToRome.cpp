#include "../library/header.hpp"
#include "../library/point_int.hpp"

int dir[8][2] = {
        {1,  2},
        {1,  -2},
        {-1, 2},
        {-1, -2},
        {2,  1},
        {2,  -1},
        {-2, 1},
        {-2, -1}
};

class JxustC2019ProComeToRome {
public:
    void solve(std::istream &in, std::ostream &out) {
        map<pair<int, int>, bool> visited;
        Point2D start;
        in >> start.x >> start.y;
        start.step = 0;
        Point2D target;
        in >> target.x >> target.y;

        queue<Point2D> q;
        q.push(start);
        visited[make_pair(start.x, start.y)] = true;

        while (!q.empty()) {
            Point2D cur = q.front();
            q.pop();
            if (cur.step > 100) {
                out << -1 << endl;
                break;
            }
            if (cur == target) {
                out << cur.step << endl;
                return;
            }
            TIMES(dir_id, 8) {
                Point2D next(cur.x + dir[dir_id][0], cur.y + dir[dir_id][1], cur.step + 1);
                if (!visited[make_pair(next.x, next.y)]) {
                    q.push(next);
                    visited[make_pair(next.x, next.y)] = true;
                }
            }
        }
    }
};
