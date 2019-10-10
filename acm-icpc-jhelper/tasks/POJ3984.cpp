#include "../library/header.hpp"
#include "../library/array.hpp"
#include "../library/point_int.hpp"

int dir[4][2] = {
        {1,  0},
        {-1, 0},
        {0,  1},
        {0,  -1}
};

class POJ3984 {
public:
    void solve(std::istream &in, std::ostream &out) {
        bool visited[7][7];
        Point2D prev[7][7];
        TIMES(i, 7) {
            TIMES(j, 7) {
                visited[i][j] = true;
            }
        }

        FOR(int, i, 1, 5, 1) {
            FOR(int, j, 1, 5, 1) {
                int tmp;
                in >> tmp;
                visited[i][j] = tmp == 1;
            }
        }

        prev[1][1].x = 0;
        prev[1][1].y = 0;
        visited[1][1] = true;

        queue<Point2D> q;
        q.push(Point2D(1, 1, 0));
        while (!q.empty()) {
            Point2D cur = q.front();
            q.pop();
            TIMES(dir_id, 4) {
                Point2D next(
                        cur.x + dir[dir_id][0],
                        cur.y + dir[dir_id][1],
                        cur.step + 1
                );
                if (!visited[next.x][next.y]) {
                    visited[next.x][next.y] = true;
                    q.push(next);
                    prev[next.x][next.y].x = cur.x;
                    prev[next.x][next.y].y = cur.y;
                    prev[next.x][next.y].step = cur.step + 1;
                }
            }
        }

        stack<Point2D> ans_stack;
        Point2D current(5, 5, prev[5][5].step);
        while (current.x + current.y > 0) {
            ans_stack.push(current);
            Point2D prev_node(prev[current.x][current.y].x, prev[current.x][current.y].y,
                         prev[current.x][current.y].step - 1);
            current.x = prev_node.x;
            current.y = prev_node.y;
            current.step = prev_node.step;
        }

        while (!ans_stack.empty()) {
            Point2D current = ans_stack.top();
            ans_stack.pop();
            out << "(" << current.x - 1 << ", " << current.y - 1 << ")" << endl;
        }
    }
};
