#ifndef DRAW_H
#define DRAW_H

#include <QGraphicsScene>

enum color_code_t
{
    BLACK,
    WHITE
};

struct canvas_t
{
    QGraphicsScene *scene;
    int width;
    int height;
};

void draw_line(const int x1, const int y1,
               const int x2, const int y2,
               const canvas_t &canvas);

void clear_canvas(const canvas_t &canvas);

#endif // DRAW_H
