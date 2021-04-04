#include "draw.h"

QPen get_pen(const color_code_t color)
{
    static QPen pen;

    switch (color)
    {
    case WHITE:
        pen.setColor(Qt::white);
        break;
    case RED:
        pen.setColor(Qt::red);
        break;
    case YELLOW:
        pen.setColor(Qt::yellow);
        break;
    case GREEN:
        pen.setColor(Qt::green);
        break;
    case BLUE:
        pen.setColor(Qt::blue);
        break;
    case CYAN:
        pen.setColor(Qt::cyan);
        break;
    case PURPLE:
        pen.setColor(Qt::darkMagenta);
        break;
    default:
        pen.setColor(Qt::black);
        break;
    }

    return pen;
}

void draw_line(const int x1, const int y1,
               const int x2, const int y2,
               const canvas_t &canvas)
{
    QPen pen = get_pen(canvas.color);
    canvas.scene->addLine(x1, y1, x2, y2, pen);
}

void clear_canvas(const canvas_t &canvas)
{
    canvas.scene->clear();
}
