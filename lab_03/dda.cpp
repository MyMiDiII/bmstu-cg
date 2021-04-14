#include <math.h>

#include "dda.h"

using namespace std;


int dda(const point_t begin, const point_t end, canvas_t &canvas,
        const algorithm_mode_t mode)
{
    int dx = end.x - begin.x;
    int dy = end.y - begin.y;

    int len = max(abs(dx), abs(dy));

    if (!len)
    {
        if (DRAW_MODE == mode)
            draw_point(begin.x, begin.y, canvas);
        return 0;
    }

    double xinc = (double) dx / len;
    double yinc = (double) dy / len;

    double x = begin.x;
    double y = begin.y;
    double x_prev = x;
    double y_prev = y;
    int steps = 0;

    for (int i = 0; i < len; ++i)
    {
        double round_x = round(x);
        double round_y = round(y);

        if (DRAW_MODE == mode)
            draw_point(round_x, round_y, canvas);

        x += xinc;
        y += yinc;

        if (STEP_MODE == mode)
        {
            steps += (round_x != x_prev && round_y != y_prev) ? 1 : 0;
            x_prev = round_x;
            y_prev = round_y;
        }
    }

    return steps;
}

int dda_draw(const segment_t &segment, canvas_t &canvas)
{
    return dda(segment.begin, segment.end, canvas, DRAW_MODE);
}
