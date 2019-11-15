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
#include <string.h>
#include <string>
using namespace std;


#define TIMES(id, size) for(int id = 0; id < (size); ++id)
#define FOR(type_id, id, from, to, step) for(type_id id = (from); id <= (to); id += step)
#define DBG(x) (void)(cout << "L" << __LINE__ << ": " << #x << " = " << (x) << '\n')

#ifndef _STDINT_H
#define _STDINT_H	1

#ifndef _UINT8_T
#define _UINT8_T
typedef unsigned char uint8_t;
#endif /* _UINT8_T */

#ifndef _UINT16_T
#define _UINT16_T
typedef unsigned short uint16_t;
#endif /* _UINT16_T */

#ifndef _UINT32_T
#define _UINT32_T
typedef unsigned int uint32_t;
#endif /* _UINT32_T */

#ifndef _UINT64_T
#define _UINT64_T
typedef unsigned long long uint64_t;
#endif /* _UINT64_T */

#ifndef _INT8_T
#define _INT8_T
typedef signed char           int8_t;
#endif /* _INT8_T */

#ifndef _INT16_T
#define _INT16_T
typedef short                   int16_t;
#endif /* _INT16_T */

#ifndef _INT32_T
#define _INT32_T
typedef int                     int32_t;
#endif /* _INT32_T */

#ifndef _INT64_T
#define _INT64_T
typedef long long               int64_t;
#endif /* _INT64_T */

#endif