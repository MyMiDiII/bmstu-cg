#include "steps.h"
#include "brezenham.h"

#define LEN 500

using namespace std;

int (*count_steps_funcs[ALGORITHM_NUM - 1])(
        const point_t begin, const point_t end,
        canvas_t &canvas,
        const algorithm_mode_t mode) = { dda,
        real_brezenham, int_brezenham, smoothing_brezenham, wu};

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

        point_t begin = { .x = 0, .y = 0 };
        point_t end = { .x = x, .y = y };
        canvas_t canvas;

        int steps = count_steps_funcs[code - 1](begin, end, canvas, STEP_MODE);

        series->append(angle, steps);
    }
}
