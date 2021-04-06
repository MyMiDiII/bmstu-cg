#include <cmath>
#include "brezenham.h"

#define EPS 1e-6

using namespace std;

inline int sign(const int num)
{
    if (num > 0)
        return 1;

    if (num < 0)
        return -1;

    return 0;
}

int real_brezenham(const point_t begin, const point_t end,
                   canvas_t &canvas,
                   const algorithm_mode_t mode)
{
    int dx = end.x - begin.x;
    int dy = end.y - begin.y;

    if (!max(abs(dx), abs(dy)))
    {
        if (DRAW_MODE == mode)
            draw_point(begin.x, begin.y, canvas);
        return 0;
    }

    int sign_x = sign(dx);
    int sign_y = sign(dy);

    dx = abs(dx);
    dy = abs(dy);

    bool swap_flag = false;
    if (dy > dx)
    {
        int temp = dx;
        dx = dy;
        dy = temp;

        swap_flag = true;
    }

    double angle_tan = (double) dy / dx;
    double err = angle_tan - 0.5;

    int cur_x = begin.x;
    int cur_y = begin.y;
    int prev_x = cur_x;
    int prev_y = cur_y;
    int steps = 0;

    for (int i = 0; i < dx; ++i)
    {
        if (DRAW_MODE == mode)
            draw_point(cur_x, cur_y, canvas);

        if (err > 0. || abs(err) < EPS)
        {
            if (swap_flag)
                cur_x += sign_x;
            else
                cur_y += sign_y;

            err -= 1;
        }

        if (swap_flag)
            cur_y += sign_y;
        else
            cur_x += sign_x;

        err += angle_tan;

        steps += (cur_x != prev_x && cur_y != prev_y) ? 1 : 0;
        prev_x = cur_x;
        prev_y = cur_y;
    }

    return steps;
}

int real_brezenham_draw(const segment_t &segment, canvas_t &canvas)
{
    return real_brezenham(segment.begin, segment.end, canvas, DRAW_MODE);
}

int int_brezenham(const point_t begin, const point_t end,
                  canvas_t &canvas,
                  const algorithm_mode_t mode)
{
    int dx = end.x - begin.x;
    int dy = end.y - begin.y;

    if (!max(abs(dx), abs(dy)))
    {
        if (DRAW_MODE == mode)
            draw_point(begin.x, begin.y, canvas);
        return 0;
    }

    int sign_x = sign(dx);
    int sign_y = sign(dy);

    dx = abs(dx);
    dy = abs(dy);

    bool swap_flag = false;
    if (dy > dx)
    {
        int temp = dx;
        dx = dy;
        dy = temp;

        swap_flag = true;
    }

    int dx_twice = 2 * dx;
    int dy_twice = 2 * dy;

    int err = dy_twice - dx;

    int cur_x = begin.x;
    int cur_y = begin.y;
    int prev_x = cur_x;
    int prev_y = cur_y;
    int steps = 0;

    for (int i = 0; i < dx; ++i)
    {
        if (DRAW_MODE == mode)
            draw_point(cur_x, cur_y, canvas);

        if (err >= 0)
        {
            if (swap_flag)
                cur_x += sign_x;
            else
                cur_y += sign_y;

            err -= dx_twice;
        }

        if (swap_flag)
            cur_y += sign_y;
        else
            cur_x += sign_x;

        err += dy_twice;

        steps += (cur_x != prev_x && cur_y != prev_y) ? 1 : 0;
        prev_x = cur_x;
        prev_y = cur_y;
    }

    return steps;
}

int int_brezenham_draw(const segment_t &segment, canvas_t &canvas)
{
    return int_brezenham(segment.begin, segment.end, canvas, DRAW_MODE);
}


int smoothing_brezenham(const point_t begin, const point_t end,
                        canvas_t &canvas,
                        const algorithm_mode_t mode)
{
    int dx = end.x - begin.x;
    int dy = end.y - begin.y;

    if (!max(abs(dx), abs(dy)))
    {
        if (DRAW_MODE == mode)
            draw_point(begin.x, begin.y, canvas);
        return 0;
    }

    int sign_x = sign(dx);
    int sign_y = sign(dy);

    dx = abs(dx);
    dy = abs(dy);

    bool swap_flag = false;
    if (dy > dx)
    {
        int temp = dx;
        dx = dy;
        dy = temp;

        swap_flag = true;
    }

    double angle_tan = (double) dy / dx;
    double err = 0.5;
    double W = 1 - angle_tan;

    int cur_x = begin.x;
    int cur_y = begin.y;
    int prev_x = cur_x;
    int prev_y = cur_y;
    int steps = 0;

    if (DRAW_MODE == mode)
    {
        canvas.color.intensity = 255 * err;
        draw_point(cur_x, cur_y, canvas);
    }

    for (int i = 1; i < dx; ++i)
    {
        if (err < W)
        {
            if (swap_flag)
                cur_y += sign_y;
            else
                cur_x += sign_x;

            err += angle_tan;
        }
        else
        {
            cur_x += sign_x;
            cur_y += sign_y;
            err -= W;
        }

        if (DRAW_MODE == mode)
        {
            canvas.color.intensity = 255 * err;
            draw_point(cur_x, cur_y, canvas);
        }

        steps += (cur_x != prev_x && cur_y != prev_y) ? 1 : 0;
        prev_x = cur_x;
        prev_y = cur_y;
    }

    return steps;
}

int smoothing_brezenham_draw(const segment_t &segment, canvas_t &canvas)
{
    return smoothing_brezenham(segment.begin, segment.end, canvas, DRAW_MODE);
}
