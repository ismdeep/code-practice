#include "../library/header.hpp"
#include "../library/point_int.hpp"
#include "../library/direction.hpp"

class TZOJ2755 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    int n, m;
	    in >> n >> m;
	    map<pair<int,int>, bool> visited;
	    Point2D start;
	    in >> start.x >> start.y;
	    start.step = 0;
	    Point2D target;
	    in >> target.x >> target.y;

	    queue<Point2D> q;
	    q.push(start);
	    visited[make_pair(start.x,start.y)] = true;

	    while (!q.empty()) {
	        Point2D cur = q.front(); q.pop();
	        if (cur.step > m) {
	            out << "Knight cannot reach Queen within " << m << " moves!" << endl;
	            break;
	        }
	        if (cur == target) {
	            out << "Knight can reach Queen within " << m << " moves!" << endl;
	            return;
	        }
	        TIMES(dir_id, 8) {
	            Point2D next( cur.x + dir_horse[dir_id][0], cur.y + dir_horse[dir_id][1], cur.step + 1 );
	            if (next.in_map(1, n, 1, n) && !visited[make_pair(next.x, next.y)]) {
                    q.push(next);
                    visited[make_pair(next.x, next.y)] = true;
	            }
	        }
	    }
	}
};
