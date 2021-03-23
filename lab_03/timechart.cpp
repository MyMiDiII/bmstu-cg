#include "timechart.h"
#include "ui_timechart.h"

#include <QtCharts/QtCharts>

TimeChart::TimeChart(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::TimeChart)
{
    ui->setupUi(this);

    QStringList algorithms;
    algorithms << "Библиотечная функция";

    QBarSet *vset = new QBarSet("What?");
    *vset << 1;

    QBarSeries *vseries = new QBarSeries;
    vseries->append(vset);

    QChart *chart = new QChart();
    chart->addSeries(vseries);

    QBarCategoryAxis *vaxis = new QBarCategoryAxis;
    vaxis->setTitleText("Алгоритм");
    vaxis->append(algorithms);

    QChartView *chartView = new QChartView(chart);
    ui->horizontalLayout->addWidget(chartView);
}

TimeChart::~TimeChart()
{
    delete ui;
}

