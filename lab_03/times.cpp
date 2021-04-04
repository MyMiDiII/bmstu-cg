#include <QGraphicsScene>
#include <chrono>
#include "times.h"

using namespace std;
using namespace chrono;

long long int get_standart_time(void)
{
    QGraphicsScene *scene = new QGraphicsScene();
    scene->setSceneRect(0, 0, 1000, 1000);
    auto start = system_clock::now();

    for (int i = 0; i < 900; i++)
        scene->addLine(0, 0, 1000, 1000);

    auto end = system_clock::now();

    return duration_cast<nanoseconds>((end - start) / 900).count();
}

err_t get_times(long long int times[ALGORITHM_NUM])
{
    times[0] = get_standart_time();

    return OK;
}
