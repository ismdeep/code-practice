#include "../library/header.hpp"
#include "../library/array.hpp"

bool is_prime(int val) {
    int stop = sqrt(val);
    FOR(int, m, 2, stop, 1) {
        if (val % m == 0) {
            return false;
        }
    }
    return true;
}

int *generate_neighbor(int value) {
    int *vals = (int *) create_array(36, sizeof(int));
    int index = -1;
    int a, b, c, d;
    int tmp = value;
    d = tmp % 10; tmp /= 10;
    c = tmp % 10; tmp /= 10;
    b = tmp % 10; tmp /= 10;
    a = tmp % 10; tmp /= 10;

    FOR(int, a_id, 1, 9, 1) {
        tmp = a_id * 1000 + b * 100 + c * 10 + d;
        if (tmp != value) { index++; vals[index] = tmp; }
    }

    TIMES(b_id, 10) {
        tmp = a * 1000 + b_id * 100 + c * 10 + d;
        if (tmp != value) { index++; vals[index] = tmp; }
    }

    TIMES(c_id, 10) {
        tmp = a * 1000 + b * 100 + c_id * 10 + d;
        if (tmp != value) { index++; vals[index] = tmp; }
    }

    TIMES(d_id, 10) {
        tmp = a * 1000 + b * 100 + c * 10 + d_id;
        if (tmp != value) { index++; vals[index] = tmp; }
    }

    return vals;
}

struct PointOnLine {
    int x;
    int step;

    PointOnLine() {}

    PointOnLine(int _x, int _step) {
        this->x = _x;
        this->step = _step;
    }

};

int count_step(int source_val, int target_val) {
    bool *visited = (bool *) create_array(10000, sizeof(bool));
    TIMES(visited_id, 10000) {
        visited[visited_id] = false;
    }

    queue<PointOnLine> q;
    q.push(PointOnLine(source_val, 0));
    visited[source_val] = true;

    while (!q.empty()) {
        PointOnLine cur = q.front();
        q.pop();
        if (cur.x == target_val) {
            free(visited);
            return cur.step;
        }
        int *next = generate_neighbor(cur.x);
        TIMES(next_id, 35) {
            if (!visited[next[next_id]] && is_prime(next[next_id])) {
                q.push(PointOnLine(next[next_id], cur.step + 1));
                visited[next[next_id]] = true;
            }
        }
        free(next);
    }
    free(visited);
    return -1;
}


class POJ3126 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    int t;
	    in >> t;
	    TIMES(t_id, t) {
	        int source_val, target_val;
	        in >> source_val >> target_val;
	        int step_count = count_step(source_val, target_val);
	        if (-1 == step_count) {
	            out << "Impossible" << endl;
	        }else {
	            out << step_count << endl;
	        }
	    }
	}
};
