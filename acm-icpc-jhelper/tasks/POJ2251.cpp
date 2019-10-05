#include "../library/header.hpp"
#include "../library/array.hpp"
#include "../library/point_int.hpp"

int dir[6][3] = {
        {1,  0,  0},
        {-1, 0,  0},
        {0,  1,  0},
        {0,  -1, 0},
        {0,  0,  1},
        {0,  0,  -1},
};

class POJ2251 {
public:
    void solve(std::istream &in, std::ostream &out) {
        int L, R, C;
        while (in >> L >> R >> C, L + R + C) {
            bool ***visited = (bool ***) create_cube(L + 2, R + 2, C + 2, sizeof(bool));
            TIMES(lid, L + 2) {
                TIMES(rid, R + 2) {
                    TIMES(cid, C + 2) {
                        visited[lid][rid][cid] = true;
                    }
                }
            }
            string str;
            Point3D start, target;
            queue<Point3D> q;
            start.step = 0;

            FOR(int, lid, 1, L, 1) {
                FOR (int, rid, 1, R, 1) {
                    in >> str;
                    FOR(int, cid, 1, C, 1) {
                        if ('S' == str[cid - 1]) {
                            start.x = lid;
                            start.y = rid;
                            start.z = cid;
                            visited[lid][rid][cid] = true;
                        } else if ('E' == str[cid - 1]) {
                            target.x = lid;
                            target.y = rid;
                            target.z = cid;
                            visited[lid][rid][cid] = false;
                        } else visited[lid][rid][cid] = '#' == str[cid - 1];
                    }
                }
            }

            q.push(start);
            int step_ans = -1;
            while (!q.empty()) {
                Point3D cur = q.front();
                q.pop();
                if (cur == target) {
                    step_ans = cur.step;
                    break;
                }
                TIMES(dir_id, 6) {
                    Point3D next(cur.x + dir[dir_id][0], cur.y + dir[dir_id][1], cur.z + dir[dir_id][2], cur.step + 1);
                    if (!visited[next.x][next.y][next.z]) {
                        q.push(next);
                        visited[next.x][next.y][next.z] = true;
                    }
                }
            }
            if (-1 == step_ans) {
                out << "Trapped!" << endl;
            } else {
                out << "Escaped in " << step_ans << " minute(s)." << endl;
            }
        }
    }
};
