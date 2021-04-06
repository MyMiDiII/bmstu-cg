#include <QGraphicsScene>
#include <chrono>
#include "times.h"
#include "draw.h"

#define RUN_COUNT 1000

using namespace std;
using namespace chrono;


long long int get_time(
        int (*algorithm)(const point_t, const point_t,
                         canvas_t &, const algorithm_mode_t mode))
{
    QGraphicsScene *scene = new QGraphicsScene();
    scene->setSceneRect(0, 0, 1000, 1000);

    color_t color = { .color = BLACK, .intensity = 255 };

    canvas_t canvas = {.scene = scene, .color = color, .width = 1000, .height = 1000};
    point_t beginp = {.x = 0, .y = 0};
    point_t endp = {.x = 1000, .y = 1000};

    auto start = system_clock::now();

    for (int i = 0; i < RUN_COUNT; i++)
        algorithm(beginp, endp, canvas, TIME_MODE);

    auto end = system_clock::now();

    return duration_cast<nanoseconds>((end - start) / RUN_COUNT).count();
}

err_t get_times(long long int times[ALGORITHM_NUM])
{
    times[STANDART] = get_time(standart_draw_line);
    times[DDA] = get_time(dda);
    times[REAL_BREZENHAM] = get_time(real_brezenham);
    times[INT_BREZENHAM] = get_time(int_brezenham);
    times[SMOOTHING_BREZENHAM] = get_time(smoothing_brezenham);

    return OK;
}
