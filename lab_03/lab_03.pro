QT       += core gui
QT       += charts

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++11

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    brezenham.cpp \
    dda.cpp \
    draw.cpp \
    errors.cpp \
    main.cpp \
    mainwindow.cpp \
    requests.cpp \
    segments.cpp \
    spectrum.cpp \
    stepchart.cpp \
    steps.cpp \
    timechart.cpp \
    times.cpp

HEADERS += \
    brezenham.h \
    dda.h \
    draw.h \
    errors.h \
    mainwindow.h \
    requests.h \
    segments.h \
    spectrum.h \
    stepchart.h \
    steps.h \
    timechart.h \
    times.h

FORMS += \
    mainwindow.ui \
    stepchart.ui \
    timechart.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target
