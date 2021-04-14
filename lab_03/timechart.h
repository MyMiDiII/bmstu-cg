#ifndef TIMECHART_H
#define TIMECHART_H

#include <QDialog>
#include <QtCharts/QtCharts>

namespace Ui {
class TimeChart;
}

class TimeChart : public QDialog
{
    Q_OBJECT

public:
    explicit TimeChart(QWidget *parent = nullptr);
    ~TimeChart();

private:
    void setHaxisGap(QBarSet *vset);
    void create_chart();
    Ui::TimeChart *ui;
};

#endif // TIMECHART_H
