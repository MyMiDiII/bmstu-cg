#include <cmath>

#include "dda.h"

using namespace std;

void dda(const point_t begin, const point_t end, const canvas_t &canvas)
{
    double dx = end.x - begin.x;
    double dy = end.y - begin.y;

    double len = max(abs(dx), abs(dy));

    if (!len)
    {
        draw_point(begin.x, begin.y, canvas);
        return ;
    }

    dx = dx / len;
    dy = dy / len;

    double x = begin.x;
    double y = begin.y;

    for (int i = 0; i < len; ++i)
    {
        double round_x = round(x);
        double round_y = round(y);
        draw_point(round_x, round_y, canvas);
        x += dx;
        y += dy;
    }
}

void dda_draw(const segment_t &segment, const canvas_t &canvas)
{
    dda(segment.begin, segment.end, canvas);
}
