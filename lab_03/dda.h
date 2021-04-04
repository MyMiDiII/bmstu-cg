#ifndef DDA_H
#define DDA_H

#include "segments.h"
#include "draw.h"

void dda_draw(const segment_t &segment, const canvas_t &canvas);

void dda(const point_t begin, const point_t end, const canvas_t &canvas);

#endif // DDA_H
