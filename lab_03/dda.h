#ifndef DDA_H
#define DDA_H

#include "segments.h"
#include "draw.h"

int dda_draw(const segment_t &segment, canvas_t &canvas);

int dda(const point_t begin, const point_t end, canvas_t &canvas,
        const algorithm_mode_t mode = DRAW_MODE);

#endif // DDA_H
