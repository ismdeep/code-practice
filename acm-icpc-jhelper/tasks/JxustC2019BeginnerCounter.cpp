#include "../library/header.hpp"

void initial(uint64_t N[], uint64_t S[], uint64_t A[]) {
    uint64_t t;
    uint64_t d = 1;
    N[0] = 0;
    S[0] = 0;
    A[0] = 1;
    for (t = 1; t < 10; t++) {
        N[t] = N[t - 1] + t * 9 * d;
        S[t] = (N[t - 1] + t + N[t]) * 9 * d / 2;
        A[t] = 9 * d;
        d *= 10;
    }
    for (t = 1; t < 9; t++) {
        S[t + 1] += S[t];
    }
}

uint8_t bS(uint64_t N[], uint64_t S[], uint64_t A[], uint64_t k)
{
    uint64_t a;
    uint64_t B;
    uint64_t C;
    uint64_t o = 0;
    uint64_t c;
    uint64_t t = 9;
    uint64_t temp;
    uint8_t r = 0;
    while (o < t)
    {
        c = (o + t) / 2;
        if (S[c] < k)
        {
            o = c + 1;
        }
        else
        {
            t = c;
        }
    }
    if (S[o] >= k)
    {
        o--;
        t--;
    }
    k -= S[o];
    temp = t;
    o = 0;
    t = A[t + 1];
    while (o < t)
    {
        c = (o + t) / 2;
        if ((N[temp] + temp + 1 + N[temp] + c * temp + c) * c / 2 < k)
        {
            o = c + 1;
        }
        else
        {
            t = c;
        }
    }
    if ((N[temp] + temp + 1 + N[temp] + o * temp + o) * o / 2 >= k)
    {
        o--;
        t--;
    }
    k -= (N[temp] + temp + 1 + N[temp] + o * temp + o) * o / 2;
    B = 1;
    for (a = 1; a * A[a] < k; a++)
    {
        k -= a * A[a];
        B *= 10;
    }
    if (k % a)
    {
        B += k / a;
        C = a - k % a + 1;
    }
    else
    {
        B += k / a - 1;
        C = 1;
    }
    while (C)
    {
        r = B % 10;
        B /= 10;
        C--;
    }
    return r;
}

class JxustC2019BeginnerCounter {
public:
    void solve(std::istream &in, std::ostream &out) {
        uint64_t counter1[10];
        uint64_t counter2[10];
        uint64_t counter3[10];
        uint64_t k;
        uint8_t R;
        initial(counter1, counter2, counter3);
        in >> k;
        out << (uint32_t)bS(counter1, counter2, counter3, k) << endl;
    }
};
