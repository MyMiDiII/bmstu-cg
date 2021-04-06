#ifndef BREZENHAM_H
#define BREZENHAM_H

#include "segments.h"
#include "draw.h"

inline int sign(const int num);

int real_brezenham_draw(const segment_t &segment, canvas_t &canvas);

int real_brezenham(const point_t begin, const point_t end,
                   canvas_t &canvas,
                   const algorithm_mode_t mode = DRAW_MODE);

int int_brezenham_draw(const segment_t &segment, canvas_t &canvas);

int int_brezenham(const point_t begin, const point_t end,
                  canvas_t &canvas,
                  const algorithm_mode_t mode);

int smoothing_brezenham_draw(const segment_t &segment, canvas_t &canvas);

int smoothing_brezenham(const point_t begin, const point_t end,
                        canvas_t &canvas,
                        const algorithm_mode_t mode);

#endif // BREZENHAM_H
