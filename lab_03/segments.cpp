#include "segments.h"


void standart_draw_line(const point_t begin, const point_t end,
                        const canvas_t &canvas)
{
    draw_line(begin.x, begin.y, end.x, end.y, canvas);
}


void standart_segment_draw(const segment_t &segment, const canvas_t &canvas)
{
    standart_draw_line(segment.begin, segment.end, canvas);
}


err_t get_segment(const segment_request_t &segment_config)
{
    switch (segment_config.algorithm)
    {
    case STANDART:
        standart_segment_draw(segment_config.segment, segment_config.canvas);
        break;
    case DDA:
        dda(segment_config.segment, segment_config.canvas);
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
