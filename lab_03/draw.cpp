#include "draw.h"

QPen get_pen(const color_t color)
{
    static QPen pen;

    switch (color.color)
    {
    case WHITE:
        pen.setColor(QColor(255, 255, 255, color.intensity));
        break;
    case RED:
        pen.setColor(QColor(255, 0, 0, color.intensity));
        break;
    case YELLOW:
        pen.setColor(QColor(255, 255, 0, color.intensity));
        break;
    case GREEN:
        pen.setColor(QColor(0, 255, 0, color.intensity));
        break;
    case BLUE:
        pen.setColor(QColor(0, 0, 255, color.intensity));
        break;
    case CYAN:
        pen.setColor(QColor(0, 255, 255, color.intensity));
        break;
    case PURPLE:
        pen.setColor(QColor(255, 0, 255, color.intensity));
        break;
    default:
        pen.setColor(QColor(0, 0, 0, color.intensity));
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

void draw_point(const int x, const int y, const canvas_t &canvas)
{
    QPen pen = get_pen(canvas.color);
    canvas.scene->addLine(x, y, x, y, pen);
}

void clear_canvas(const canvas_t &canvas)
{
    canvas.scene->clear();
}
