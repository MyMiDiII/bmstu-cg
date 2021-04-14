#include "segments.h"
#include "dda.h"
#include "brezenham.h"
#include "wu.h"

int standart_draw_line(const point_t begin, const point_t end,
                       canvas_t &canvas,
                       const algorithm_mode_t mode)
{
    draw_line(begin.x, begin.y, end.x, end.y, canvas);
    return mode;
}


void standart_segment_draw(const segment_t &segment, canvas_t &canvas)
{
    standart_draw_line(segment.begin, segment.end, canvas, DRAW_MODE);
}


err_t get_segment(segment_request_t &segment_config)
{
    switch (segment_config.algorithm)
    {
    case STANDART:
        standart_segment_draw(segment_config.segment, segment_config.canvas);
        break;
    case DDA:
        dda_draw(segment_config.segment, segment_config.canvas);
        break;
    case REAL_BREZENHAM:
        real_brezenham_draw(segment_config.segment, segment_config.canvas);
        break;
    case INT_BREZENHAM:
        int_brezenham_draw(segment_config.segment, segment_config.canvas);
        break;
    case SMOOTHING_BREZENHAM:
        smoothing_brezenham_draw(segment_config.segment, segment_config.canvas);
        break;
    case WU:
        wu_draw(segment_config.segment, segment_config.canvas);
        break;
    default:
        break;
    }

    return OK;
}

point_t move_point(const point_t &begin, const point_t &point)
{
    point_t new_point = {.x = point.x + begin.x, .y = point.y + begin.y};
    return new_point;
}

void points_arr_init(points_arr_t &points)
{
    points.arr = NULL;
    points.len = 0;
    points.capacity = 0;
}

void destroy_points_arr(points_arr_t &points)
{
    free(points.arr);
    points_arr_init(points);
}
