#include "../library/header.hpp"
#include "../library/point_int.hpp"
#include "../library/direction.hpp"

class Map {
public:
    int row_size, col_size;
    int shortest_path;
    Point2D start;
    Point2D end;

    char **data;
    bool **used;

    void create_map_data() {
        this->data = (char **) malloc(this->row_size * sizeof(char *));
        TIMES(row_id, this->row_size) {
            this->data[row_id] = (char *) malloc(this->col_size * sizeof(char));
        }

        this->used = (bool **) malloc(this->row_size * sizeof(bool *));
        TIMES(row_id, this->row_size) {
            this->used[row_id] = (bool *) malloc(this->col_size * sizeof(bool));
        }
        TIMES(row_id, this->row_size) {
            TIMES(col_id, this->col_size) {
                this->used[row_id][col_id] = false;
            }
        }
    }

    void dfs(Point2D *cur) {
        if (cur->x == this->end.x && cur->y == this->end.y) {
            if (cur->step < this->shortest_path) {
                this->shortest_path = cur->step;
            }
            return;
        }

        TIMES(direction_id, 4) {
            Point2D next(cur->x + dir4[direction_id][0], cur->y + dir4[direction_id][1], cur->step + 1);
            if (next.in_map(0, this->row_size - 1, 0, this->col_size - 1) && '-' == this->data[next.x][next.y] &&
                !used[next.x][next.y]) {
                used[next.x][next.y] = true;
                dfs(&next);
                used[next.x][next.y] = false;
            }
        }
    }
};

class JustOJ1476 {
public:

    void solve(std::istream &in, std::ostream &out) {
        int case_count;
        in >> case_count;
        TIMES(case_id, case_count) {
            Map _map_;
            in >> _map_.row_size >> _map_.col_size;
            _map_.shortest_path = _map_.row_size * _map_.col_size;
            _map_.create_map_data();
            TIMES(row_id, _map_.row_size) {
                string str;
                in >> str;
                TIMES(col_id, _map_.col_size) {
                    _map_.data[row_id][col_id] = str[col_id];
                    if ('S' == _map_.data[row_id][col_id]) {
                        _map_.start.x = row_id;
                        _map_.start.y = col_id;
                    }
                    if ('E' == _map_.data[row_id][col_id]) {
                        _map_.end.x = row_id;
                        _map_.end.y = col_id;
                        _map_.data[row_id][col_id] = '-';
                    }
                }
            }
            Point2D start_point(_map_.start.x, _map_.start.y, 0);
            _map_.dfs(&start_point);
            out << _map_.shortest_path << endl;
        }
    }
};
