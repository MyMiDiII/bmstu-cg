#include "mainwindow.h"
#include "ui_mainwindow.h"


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    QGraphicsScene *scene = new QGraphicsScene(this);
    scene->setSceneRect(0, 0, 998, 874);
    ui->graphicsView->setScene(scene);
}

MainWindow::~MainWindow()
{
    delete ui;
}

canvas_t MainWindow::init_canvas()
{
    static canvas_t canvas;

    canvas.scene = ui->graphicsView->scene();
    canvas.color = (color_code_t) ui->comboBox_color->currentIndex();
    canvas.width = canvas.scene->width();
    canvas.height = canvas.scene->height();

    return canvas;
}

void MainWindow::read_begin(point_t &point)
{
    point.x = ui->spinBox_xb->value();
    point.y = ui->spinBox_yb->value();
}

void MainWindow::read_end(point_t &point)
{
    point.x = ui->spinBox_xe->value();
    point.y = ui->spinBox_ye->value();
}

void MainWindow::read_segment(segment_t &segment)
{
    read_begin(segment.begin);
    read_end(segment.end);
}

void MainWindow::create_segment_config(segment_request_t &config)
{
    config.algorithm = (algorithm_code_t) ui->comboBox_algorithm->currentIndex();
    config.canvas = init_canvas();
    read_segment(config.segment);
}

void MainWindow::on_btn_segment_clicked()
{
    request_t request;
    request.code = SEGMENT;
    create_segment_config(request.segment_config);

    handle_request(request);
}

void MainWindow::read_spectrum(spectrum_t &spectrum)
{
    spectrum.len = ui->spinBox_len->value();
    spectrum.num = ui->spinBox_num->value();
}

void MainWindow::create_spectrum_config(spectrum_request_t &config)
{
    config.algorithm = (algorithm_code_t) ui->comboBox_algorithm->currentIndex();
    config.canvas = init_canvas();
    read_spectrum(config.spectrum);
}

void MainWindow::on_btn_spectrum_clicked()
{
    request_t request;
    request.code = SPECTRUM;
    create_spectrum_config(request.spectrum_config);

    handle_request(request);
}

void MainWindow::on_btn_time_clicked()
{
    TimeChart *timechart = new TimeChart();
    timechart->show();
}

void MainWindow::on_btn_clear_clicked()
{
    request_t request = {.code = CLEAR};
    request.clear_config = init_canvas();

    handle_request(request);
}


void MainWindow::on_comboBox_color_currentIndexChanged(int index)
{
    switch (index)
    {
    case 0:
        ui->lbl_color->setStyleSheet("background: black");
        break;
    case 1:
        ui->lbl_color->setStyleSheet("background: white");
        break;
    case 2:
        ui->lbl_color->setStyleSheet("background: red");
        break;
    case 3:
        ui->lbl_color->setStyleSheet("background: yellow");
        break;
    case 4:
        ui->lbl_color->setStyleSheet("background: rgb(45, 255, 0)");
        break;
    case 5:
        ui->lbl_color->setStyleSheet("background: cyan");
        break;
    case 6:
        ui->lbl_color->setStyleSheet("background: blue");
        break;
    case 7:
        ui->lbl_color->setStyleSheet("background: darkMagenta");
        break;
    default:
        break;
    }
}

void MainWindow::on_btn_gradation_clicked()
{
    StepChart *stepchart = new StepChart();
    stepchart->showMaximized();
}
