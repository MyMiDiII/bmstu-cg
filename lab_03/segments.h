#ifndef SEGMENTS_H
#define SEGMENTS_H

#include "errors.h"
#include "draw.h"

struct point_t
{
    int x;
    int y;
};

struct segment_t
{
    point_t begin;
    point_t end;
};

enum algorithm_code_t
{
    STANDART,
    DDA,
    REAL_BREZENHAM,
    INT_BREZENHAM,
    SMOOTHING_BREZENHAM,
    WU
};

struct segment_request_t
{
    canvas_t canvas;
    algorithm_code_t algorithm;
    segment_t segment;
};

struct points_arr_t
{
    point_t *arr;
    size_t len;
    size_t capacity;
};

err_t get_segment(segment_request_t &segment_config);

void destroy_points_arr(points_arr_t &points);

void points_arr_init(points_arr_t &points);

int standart_draw_line(const point_t begin, const point_t end,
                       canvas_t &canvas,
                       const algorithm_mode_t mode = DRAW_MODE);

point_t move_point(const point_t &begin, const point_t &point);

#endif // SEGMENTS_H
