#include "draw.h"

void draw_line(const int x1, const int y1,
               const int x2, const int y2,
               const canvas_t &canvas)
{
    canvas.scene->addLine(x1, y1, x2, y2);
}

void clear_canvas(const canvas_t &canvas)
{
    canvas.scene->clear();
}
