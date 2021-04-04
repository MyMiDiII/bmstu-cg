#include "timechart.h"
#include "ui_timechart.h"

#include <QtCharts/QtCharts>

#include "requests.h"

TimeChart::TimeChart(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::TimeChart)
{
    ui->setupUi(this);

    QStringList algorithms;
    algorithms << "Библиотечная функция";

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
    haxis->setTitleText("Время");
    chart->addAxis(haxis, Qt::AlignLeft);
    vseries->attachAxis(haxis);

    QChartView *chartView = new QChartView(chart);
    ui->horizontalLayout->addWidget(chartView);
}

TimeChart::~TimeChart()
{
    delete ui;
}

