#include "../library/header.hpp"
#include "../library/point_int.hpp"
#include "../library/array.hpp"
#include "../library/direction.hpp"

void bfs_map(bool **visited, Point2D *start, bool **is_kfc, int** step_count) {
    visited[start->x][start->y] = true;
    queue<Point2D> q;
    q.push(*start);
    while (!q.empty()) {
        Point2D cur = q.front(); q.pop();
        step_count[cur.x][cur.y] = cur.step;
        TIMES(dir_id, 4) {
            Point2D next(cur.x + dir4[dir_id][0], cur.y + dir4[dir_id][1], cur.step + 1);
            if (!visited[next.x][next.y]) {
                q.push(next);
                visited[next.x][next.y] = true;
            }
        }
    }
}

void init(std::istream &in, bool **visited_y, bool **visited_m, int **step_count_y, int **step_count_m, int n, int m, bool **is_kfc, Point2D &point_y, Point2D &point_m) {
    TIMES(i, n + 2) {
        TIMES(j, m + 2) {
            visited_y[i][j] = true;
            visited_m[i][j] = true;
            is_kfc[i][j] = false;
        }
    }
    /* Input START */
    string str;
    FOR (int, i, 1, n, 1) {
        in >> str;
        FOR (int, j, 1, m, 1) {
            step_count_y[i][j] = 0x3fffffff;
            step_count_m[i][j] = 0x3fffffff;
            if ('Y' == str[j - 1]) {
                point_y.x = i;
                point_y.y = j;
                point_y.step = 0;
                visited_y[i][j] = true;
                visited_m[i][j] = false;
            } else if ('M' == str[j - 1]) {
                point_m.x = i;
                point_m.y = j;
                point_m.step = 0;
                visited_y[i][j] = false;
                visited_m[i][j] = true;
            } else if ('@' == str[j-1]) {
                is_kfc[i][j] = true;
                visited_y[i][j] = false;
                visited_m[i][j] = false;
            } else if ('#' == str[j-1]) {
                visited_y[i][j] = true;
                visited_m[i][j] = true;
            } else {
                visited_y[i][j] = false;
                visited_m[i][j] = false;
            }
        }
    }
    /* Input END */
}


class HDU2612 {
public:
    void solve(std::istream &in, std::ostream &out) {
        int n, m;
        string str;
        while (in >> n >> m) {
            bool **visited_y = (bool **) create_matrix(n + 2, m + 2, sizeof(bool));
            bool **visited_m = (bool **) create_matrix(n + 2, m + 2, sizeof(bool));
            bool **is_kfc    = (bool **) create_matrix(n + 2, m + 2, sizeof(bool));
            int **step_count_y = (int **) create_matrix(n + 2, m + 2, sizeof(int));
            int **step_count_m = (int **) create_matrix(n + 2, m + 2, sizeof(int));
            Point2D point_y;
            Point2D point_m;

            init(in, visited_y, visited_m, step_count_y, step_count_m, n, m, is_kfc, point_y, point_m);

            bfs_map(visited_y, &point_y, is_kfc, step_count_y);
            bfs_map(visited_m, &point_m, is_kfc, step_count_m);

            int ans = 0x3fffffff;
            FOR (int, i, 1, n, 1) {
                FOR (int, j, 1, m, 1) {
                    if (is_kfc[i][j]) {
                        ans = min(ans, step_count_m[i][j] + step_count_y[i][j]);
                    }
                }
            }
            out << ans * 11 << endl;
        }
    }
};
