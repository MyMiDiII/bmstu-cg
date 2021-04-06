#include "stepchart.h"
#include "ui_stepchart.h"

#include <QtCharts/QtCharts>
#include "times.h"
#include "requests.h"
#include "segments.h"

StepChart::StepChart(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::StepChart)
{
    ui->setupUi(this);

    QChart *chart = new QChart();
    chart->setTitle(QString("Исследование ступенчатости"));
    chart->setAnimationOptions(QtCharts::QChart::SeriesAnimations);

    QValueAxis *axisX = new QValueAxis();
    axisX->setTitleText("Угол");
    axisX->applyNiceNumbers();
    chart->addAxis(axisX, Qt::AlignBottom);

    QValueAxis *axisY = new QValueAxis();
    axisY->setTitleText("Количество ступенек");
    axisY->setLabelFormat("%d");
    axisY->applyNiceNumbers();
    chart->addAxis(axisY, Qt::AlignLeft);

    char names[4][100] =
        {
            "ЦДА",
            "Брезенхем (float)",
            "Брезенхем (int)",
            "Брезенхем (сглаживание)"
        };

    for (int code = 1; code < ALGORITHM_NUM; ++code)
    {
        QLineSeries *series = new QLineSeries();

        series->setName(names[code - 1]);

        find_steps(series, (algorithm_code_t)code);

        chart->addSeries(series);
        QPen pen = series->pen();
        pen.setWidth(10);
        series->setPen(pen);
        series->attachAxis(axisX);
        series->attachAxis(axisY);
    }

    chart->legend()->setVisible(true);
    chart->legend()->setAlignment(Qt::AlignBottom);

    QChartView *chartView = new QChartView(chart);
    ui->horizontalLayout->addWidget(chartView);
}

StepChart::~StepChart()
{
    delete ui;
}
