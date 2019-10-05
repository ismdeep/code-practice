struct Point2D {
    int x, y, step;

    Point2D(){}

    Point2D(int _x, int _y, int _step) {
        this->x = _x;
        this->y = _y;
        this->step = _step;
    }
    bool operator == (Point2D p) {
        return this->x == p.x && this->y == p.y;
    }

    bool in_map (int x_min, int x_max, int y_min, int y_max) {
        return x_min <= this->x && this->x <= x_max && y_min <= this->y && this->y <= y_max;
    }

    string ToString() {
        char ch[1024];
        sprintf(ch, "{x:%d, y:%d, step:%d}", this->x, this->y, this->step);
        string str = ch;
        return str;
    }
};

struct Point3D {
    int x, y, z, step;

    Point3D() {}

    Point3D(int _x, int _y, int _z, int _step) {
        this->x = _x;
        this->y = _y;
        this->z = _z;
        this->step = _step;
    }

    bool operator==(Point3D p) {
        return this->x == p.x && this->y == p.y && this->z == p.z;
    }

    string ToString() {
        char ch[1024];
        sprintf(ch, "{x:%d, y:%d, z:%d, step:%d}", this->x, this->y, this->z, this->step);
        string str = ch;
        return str;
    }
};

