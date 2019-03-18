//
// Created by ismdeep on 2019-03-18.
//
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
    std::set<int> s;
    s.insert(1);
    s.insert(1);
    s.insert(2);
    s.insert(3);
    cout << s.count(1) << endl;
    cout << s.count(5) << endl;
    cout << s.size() << endl;
    return 0;
}
