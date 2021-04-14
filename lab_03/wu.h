#ifndef WU_H
#define WU_H

#include "segments.h"
#include "draw.h"

int wu(const point_t begin, const point_t end,
       canvas_t &canvas,
       const algorithm_mode_t mode);

int wu_draw(const segment_t &segment, canvas_t &canvas);

#endif // WU_H
