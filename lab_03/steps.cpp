#include "steps.h"

#define LEN 500

using namespace std;

int count_dda_steps(int x, int y)
{
    double dx = x;
    double dy = y;

    double len = max(abs(dx), abs(dy));

    if (!len)
        return 0;

    dx = dx / len;
    dy = dy / len;

    double x_cur = 0;
    double y_cur = 0;
    double x_prev = x_cur;
    double y_prev = y_cur;
    int steps = 0;

    for (int i = 0; i < len; ++i)
    {
        double round_x = round(x_cur);
        double round_y = round(y_cur);

        steps += (round_x != x_prev && round_y != y_prev) ? 1 : 0;
        x_prev = round_x;
        y_prev = round_y;

        x_cur += dx;
        y_cur += dy;
    }

    return steps;
}

int (*count_steps_funcs[ALGORITHM_NUM - 1])(int, int) = { count_dda_steps };

void find_steps(QLineSeries *series, const algorithm_code_t code)
{
    double start_x = 500;
    double start_y = 0;

    for (int angle = 0; angle <= 90; ++angle)
    {
        double radians_angle = M_PI / 180 * angle ;
        double cos_angle = cos(radians_angle);
        double sin_angle = sin(radians_angle);

        int x = (int) (start_x * cos_angle - start_y * sin_angle);
        int y = (int) (start_x * sin_angle + start_y * cos_angle);

        int steps = count_steps_funcs[code - 1](x, y);

        series->append(angle, steps);
    }
}
