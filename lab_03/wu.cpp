#include <cmath>
#include "wu.h"

using namespace std;

double frac_part(const double num)
{
    return num - floor(num);
}

void swap(double &first, double &second)
{
    double temp = first;
    first = second;
    second = temp;
}


void draw_wu(double x, double y, double fpart, double add,
             canvas_t &canvas, bool flag)
{
    canvas.color.intensity = (1 - fpart) * add * 255;
    flag ? draw_point(y, x, canvas) : draw_point(x, y, canvas);
    canvas.color.intensity = fpart * add * 255;
    flag ? draw_point(y + 1, x, canvas) : draw_point(x, y + 1, canvas);
}

int wu(const point_t begin, const point_t end,
       canvas_t &canvas,
       const algorithm_mode_t mode)
{
    double x0 = begin.x;
    double y0 = begin.y;
    double x1 = end.x;
    double y1 = end.y;

    bool swap_flag = abs(y1 - y0) > abs(x1 - x0);

    if (swap_flag)
    {
        swap(x0, y0);
        swap(x1, y1);
    }

    if (x0 > x1)
    {
        swap(x0, x1);
        swap(y0, y1);
    }

    double dx = x1 - x0;
    double dy = y1 - y0;
    double angle_tan = dx ? (double) dy / dx : 1.;

    double xgap = 1 - frac_part(x0 + 0.5);
    double xpxl1 = x0;
    double ypxl1 = floor(y0);
    double fpart = frac_part(y0);

    if (DRAW_MODE == mode)
        draw_wu(xpxl1, ypxl1, fpart, xgap, canvas, swap_flag);

    xgap = frac_part(x1 + 0.5);
    double xpxl2 = x1;
    double ypxl2 = floor(y1);
    fpart = frac_part(y1);

    if (DRAW_MODE == mode)
        draw_wu(xpxl2, ypxl2, fpart, xgap, canvas, swap_flag);

    int steps = 0;
    double intery = y0 + angle_tan;

    for (int x = xpxl1 + 1; x < xpxl2; ++x)
    {
        double y = floor(intery);
        double fpart = frac_part(intery);

        if (DRAW_MODE == mode)
            draw_wu(x, y, fpart, 1, canvas, swap_flag);

        if (STEP_MODE == mode)
            if (y != floor(intery + angle_tan))
                ++steps;

        intery += angle_tan;
    }

    return steps;
}

int wu_draw(const segment_t &segment, canvas_t &canvas)
{
    return wu(segment.begin, segment.end, canvas, DRAW_MODE);
}
