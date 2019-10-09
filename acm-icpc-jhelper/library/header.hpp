#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <stack>
#include <vector>
#include <algorithm>
#include <list>
#include <map>
#include <queue>
#include <bitset>
#include <numeric>
#include <sstream>
#include <limits>

using namespace std;


#define TIMES(id, size) for(int id = 0; id < (size); ++id)
#define FOR(type_id, id, from, to, step) for(type_id id = (from); id <= (to); id += step)
#define DBG(x) \
    (void)(cout << "L" << __LINE__ \
    << ": " << #x << " = " \
    << (x) << '\n')

#ifndef _BITS_STDINT_UINTN_H
typedef unsigned long long uint64_t;
#endif
typedef unsigned char uint8_t;
