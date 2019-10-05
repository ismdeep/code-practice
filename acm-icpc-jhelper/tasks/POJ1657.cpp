#include "../library/header.hpp"
#include "../library/point_int.hpp"

/* 王：横、直、斜都可以走，但每步限走一格。 */
int dir_king[][2] = {
        {1,0},{-1,0},{0,1},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}
};

/* 后：横、直、斜都可以走，每步格数不受限制。 */
int dir_queue[][2] = {
        {1,0},{-1,0},{0,1},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1},
        {2,0},{-2,0},{0,2},{0,-2},{2,2},{2,-2},{-2,2},{-2,-2},
        {3,0},{-3,0},{0,3},{0,-3},{3,3},{3,-3},{-3,3},{-3,-3},
        {4,0},{-4,0},{0,4},{0,-4},{4,4},{4,-4},{-4,4},{-4,-4},
        {5,0},{-5,0},{0,5},{0,-5},{5,5},{5,-5},{-5,5},{-5,-5},
        {6,0},{-6,0},{0,6},{0,-6},{6,6},{6,-6},{-6,6},{-6,-6},
        {7,0},{-7,0},{0,7},{0,-7},{7,7},{7,-7},{-7,7},{-7,-7},
        {8,0},{-8,0},{0,8},{0,-8},{8,8},{8,-8},{-8,8},{-8,-8}
};

/* 车：横、竖均可以走，不能斜走，格数不限。 */
int dir_castle[][2] = {
        {1,0},{-1,0},{0,1},{0,-1},
        {2,0},{-2,0},{0,2},{0,-2},
        {3,0},{-3,0},{0,3},{0,-3},
        {4,0},{-4,0},{0,4},{0,-4},
        {5,0},{-5,0},{0,5},{0,-5},
        {6,0},{-6,0},{0,6},{0,-6},
        {7,0},{-7,0},{0,7},{0,-7},
        {8,0},{-8,0},{0,8},{0,-8}
};

/* 象：只能斜走，格数不限。 */
int dir_jumbo[][2] = {
        {1,1},{1,-1},{-1,1},{-1,-1},
        {2,2},{2,-2},{-2,2},{-2,-2},
        {3,3},{3,-3},{-3,3},{-3,-3},
        {4,4},{4,-4},{-4,4},{-4,-4},
        {5,5},{5,-5},{-5,5},{-5,-5},
        {6,6},{6,-6},{-6,6},{-6,-6},
        {7,7},{7,-7},{-7,7},{-7,-7},
        {8,8},{8,-8},{-8,8},{-8,-8}
};



void parse_position(string str, int *x, int *y) {
    *x = str[0] - 'a' + 1;
    *y = str[1] - '0';
}

void init_visited(bool visited[10][10]) {
    TIMES(i, 10) {
        TIMES(j,10) {
            visited[i][j] = false;
        }
    }
    TIMES(j, 10) {
        visited[0][j] = true;
        visited[9][j] = true;
    }
    TIMES(i, 10) {
        visited[i][0] = true;
        visited[i][9] = true;
    }
}

int walk_count(Point2D start, Point2D target, int dir[][2], int dir_count) {
    queue< Point2D > q;
    q.push(start);
    bool visited[10][10];
    init_visited(visited);
    visited[start.x][start.y] = true;
    while (!q.empty()) {
        Point2D cur = q.front();
        q.pop();
        if (cur == target) {
            return cur.step;
        }
        TIMES(dir_id, dir_count) {
            Point2D next(cur.x + dir[dir_id][0], cur.y + dir[dir_id][1], cur.step + 1);
            if (next.in_map(1,8,1,8) && !visited[next.x][next.y]) {
                q.push(next);
                visited[next.x][next.y] = true;
            }
        }
    }
    return -1;
}


string step_dump(int step) {
    if (-1 == step) {
        return "Inf";
    }
    stringstream ss;
    ss << step << endl;
    string str;
    ss >> str;
    return str;
}


class POJ1657 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    int t;
	    in >> t;
        string str_start, str_target;
        int start_x, start_y, target_x, target_y;
	    while (t--) {
	        in >> str_start >> str_target;
	        parse_position(str_start, &start_x, &start_y);
	        parse_position(str_target, &target_x, &target_y);
            Point2D start(start_x, start_y, 0);
            Point2D target(target_x, target_y, -1);
	        out     << step_dump(walk_count(start, target, dir_king, 8)) << " "
                    << step_dump(walk_count(start, target, dir_queue, 64)) << " "
                    << step_dump(walk_count(start, target, dir_castle, 32)) << " "
                    << step_dump(walk_count(start, target, dir_jumbo, 32)) << endl;
	    }
	}
};
