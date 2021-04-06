#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

#include "timechart.h"
#include "stepchart.h"
#include "requests.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_btn_segment_clicked();

    void on_btn_spectrum_clicked();

    void on_btn_time_clicked();

    void on_btn_clear_clicked();

    void on_comboBox_color_currentIndexChanged(int index);

    void on_btn_gradation_clicked();

private:
    color_t set_color(int index);

    canvas_t init_canvas();

    void read_begin(point_t &point);

    void read_end(point_t &point);

    void read_segment(segment_t &segment);

    void create_segment_config(segment_request_t &config);

    void read_spectrum(spectrum_t &spectrum);

    void create_spectrum_config(spectrum_request_t &config);

    Ui::MainWindow *ui;
    TimeChart *timechart;
};

#endif // MAINWINDOW_H
