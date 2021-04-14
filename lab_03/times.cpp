#include <QGraphicsScene>
#include <chrono>
#include "times.h"
#include "draw.h"
#include "spectrum.h"

#define RUN_COUNT 50

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
    point_t beginp = {.x = 500, .y = 500};
    spectrum_t spectrum = { .len = 500, .num = 360 };

    points_arr_t points;
    points_arr_init(points);
    err_t rc = get_points_set(points, spectrum);

    if (rc)
        return rc;

    for (size_t i = 0; i < points.len; i++)
    {
        points.arr[i].x += beginp.x;
        points.arr[i].y += beginp.y;
    }

    auto start = system_clock::now();

    for (int i = 0; i < RUN_COUNT; i++)
    {
        for (size_t j = 0; j < points.len; j++)
            algorithm(beginp, points.arr[i], canvas, TIME_MODE);
    }


    auto end = system_clock::now();

    destroy_points_arr(points);

    return duration_cast<microseconds>((end - start) / RUN_COUNT).count();
}

err_t get_times(long long int times[ALGORITHM_NUM])
{
    times[WU] = get_time(wu);
    times[SMOOTHING_BREZENHAM] = get_time(smoothing_brezenham);
    times[REAL_BREZENHAM] = get_time(real_brezenham);
    times[INT_BREZENHAM] = get_time(int_brezenham);
    times[STANDART] = get_time(standart_draw_line);
    times[DDA] = get_time(dda);

    return OK;
}
