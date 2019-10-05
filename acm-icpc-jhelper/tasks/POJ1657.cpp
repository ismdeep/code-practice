#include "../library/header.hpp"

struct Point{
    int x, y;

    Point(){}

    Point(int _x, int _y) {
        x = _x;
        y = _y;
    }
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


/* 王：横、直、斜都可以走，但每步限走一格。 */
int king_count(Point start, Point target) {
    queue< Point > q;
    q.push(start);
    bool visited[10][10];
    init_visited(visited);
    visited[start.x][start.y] = true;
    
    return 0;
}

/* 后：横、直、斜都可以走，每步格数不受限制。 */
int queue_count(Point start, Point target) {
    return 0;
}

/* 车：横、竖均可以走，不能斜走，格数不限。 */
int castle_count(Point start, Point target) {
    return 0;
}

/* 象：只能斜走，格数不限。 */
int jumbo_count(Point start, Point target) {
    return 0;
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
	        Point start(start_x, start_y);
	        Point target(target_x, target_y);
	        out     << king_count(start, target) << " "
                    << queue_count(start, target) << " "
                    << castle_count(start, target) << " "
                    << jumbo_count(start, target) << endl;
	    }
	}
};
