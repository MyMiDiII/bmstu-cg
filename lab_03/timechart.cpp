#include "timechart.h"
#include "ui_timechart.h"

#include "requests.h"

TimeChart::TimeChart(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::TimeChart)
{
    ui->setupUi(this);

    QStringList algorithms;
    algorithms << "Библиотечная функция";
    algorithms << "ЦДА";
    algorithms << "Брезенхем\n(float)";
    algorithms << "Брезенхем\n(int)";
    algorithms << "Брезенхем\n(с устр. ступенчатости))";
    algorithms << "Ву";

    QBarSet *vset = new QBarSet("Time");
    long long int times[ALGORITHM_NUM];
    request_t time_request = {.code = TIME, .time_config = (long long int *) &times};
    handle_request(time_request);

    for (int i = 0; i < ALGORITHM_NUM; i++)
        vset->append(time_request.time_config[i]);

    QBarSeries *vseries = new QBarSeries;
    vseries->append(vset);

    QChart *chart = new QChart();
    chart->addSeries(vseries);
    chart->legend()->hide();
    chart->setAnimationOptions(QChart::SeriesAnimations);

    QBarCategoryAxis *vaxis = new QBarCategoryAxis;
    vaxis->setTitleText("Алгоритм");
    vaxis->append(algorithms);
    chart->addAxis(vaxis, Qt::AlignBottom);
    vseries->attachAxis(vaxis);

    QValueAxis *haxis = new QValueAxis;
    setHaxisGap(vset);
    haxis->setTitleText("Время, μs");
    chart->addAxis(haxis, Qt::AlignLeft);
    vseries->attachAxis(haxis);

    QChartView *chartView = new QChartView(chart);
    ui->horizontalLayout->addWidget(chartView);
}

void TimeChart::setHaxisGap(QBarSet *vset)
{
    qint64 max_time = std::max(vset->at(WU), vset->at(DDA));
    qint64 min_time = std::min(vset->at(WU), vset->at(DDA));
    vset->replace(WU, max_time);
    vset->replace(DDA, min_time);
}

TimeChart::~TimeChart()
{
    delete ui;
}

