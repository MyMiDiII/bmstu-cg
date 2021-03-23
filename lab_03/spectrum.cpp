#include <math.h>

#include "spectrum.h"

err_t get_points_set(points_arr_t &points, const spectrum_t &spectrum)
{
    points.capacity = spectrum.num;
    points.len = spectrum.num;
    points.arr = (point_t *) malloc(sizeof(point_t) * points.capacity);

    if (!points.arr)
        return MEMORY_ERR;

    points.arr[0].x = 0;
    points.arr[0].y = -spectrum.len;

    double step = 2 * M_PI / spectrum.num;
    double angle = step;

    for (size_t i = 1; i < points.len; i++)
    {
        double cos_angle = cos(angle);
        double sin_angle = sin(angle);
        points.arr[i].x = (int) (points.arr[0].x * cos_angle -
                          points.arr[0].y * sin_angle);
        points.arr[i].y = (int) (points.arr[0].x * sin_angle +
                          points.arr[0].y * cos_angle);
        angle += step;
    }

    return OK;
}


void draw_spectrum(const canvas_t &canvas, const points_arr_t &points)
{
    point_t begin = {.x = canvas.width / 2, .y = canvas.height / 2};

    for (size_t i = 0; i < points.len; i++)
    {
        standart_draw_line(begin, move_point(begin, points.arr[i]), canvas);
    }
}


err_t get_spectrum(const spectrum_request_t &spectrum_config)
{
    points_arr_t points;
    points_arr_init(points);
    err_t rc = get_points_set(points, spectrum_config.spectrum);

    if (rc)
        return rc;

    switch (spectrum_config.algorithm)
    {
    case STANDART:
        draw_spectrum(spectrum_config.canvas, points);
        destroy_points_arr(points);
        break;
    default:
        break;
    }

    return OK;
}
