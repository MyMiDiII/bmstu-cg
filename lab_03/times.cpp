#include <QGraphicsScene>
#include <chrono>
#include "times.h"

#define RUN_COUNT 10000

using namespace std;
using namespace chrono;

long long int get_standart_time(void)
{
    QGraphicsScene *scene = new QGraphicsScene();
    scene->setSceneRect(0, 0, 1000, 1000);
    auto start = system_clock::now();

    for (int i = 0; i < RUN_COUNT; i++)
        scene->addLine(0, 0, 1000, 1000);

    auto end = system_clock::now();

    return duration_cast<nanoseconds>((end - start) / RUN_COUNT).count();
}

long long int get_dda_time(void)
{
    QGraphicsScene *scene = new QGraphicsScene();
    scene->setSceneRect(0, 0, 1000, 1000);

    canvas_t canvas = {.scene = scene, .color = BLACK, .width = 1000, .height = 1000};
    point_t beginp = {.x = 0, .y = 0};
    point_t endp = {.x = 1000, .y = 1000};

    auto start = system_clock::now();

    for (int i = 0; i < RUN_COUNT; i++)
        dda(beginp, endp, canvas);

    auto end = system_clock::now();

    return duration_cast<nanoseconds>((end - start) / RUN_COUNT).count();
}

err_t get_times(long long int times[ALGORITHM_NUM])
{
    times[0] = get_standart_time();
    times[1] = get_dda_time();

    return OK;
}
