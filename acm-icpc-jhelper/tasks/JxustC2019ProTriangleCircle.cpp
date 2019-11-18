#include "../library/header.hpp"
#include "../library/computational_geometry.hpp"

class JxustC2019ProTriangleCircle {
public:
	void solve(std::istream& in, std::ostream& out) {
	    Point pa, pb, pc;
	    in >> pa.x >> pa.y >> pb.x >> pb.y >> pc.x >> pc.y;
	    Point center = center_of_3_points(pa, pb, pc);
	    char tmp[1024];
	    sprintf(tmp, "(%.2lf,%.2lf) %.2lf", center.x, center.y, center.distance(pa));
	    string tmp_str = tmp;
	    out << tmp_str << endl;
	}
};
