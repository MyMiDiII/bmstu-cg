#ifndef STEPCHART_H
#define STEPCHART_H

#include <QDialog>
#include "steps.h"

namespace Ui {
class StepChart;
}

class StepChart : public QDialog
{
    Q_OBJECT

public:
    explicit StepChart(QWidget *parent = nullptr);
    ~StepChart();

private:
    Ui::StepChart *ui;
};

#endif // STEPCHART_H
