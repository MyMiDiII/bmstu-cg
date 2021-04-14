#ifndef SPECTRUM_H
#define SPECTRUM_H

#include "draw.h"
#include "segments.h"
#include "errors.h"
#include "dda.h"
#include "brezenham.h"
#include "wu.h"

struct spectrum_t
{
    size_t len;
    size_t num;
};

struct spectrum_request_t
{
    canvas_t canvas;
    algorithm_code_t algorithm;
    spectrum_t spectrum;
};

err_t get_spectrum(spectrum_request_t &spectrum_config);

err_t get_points_set(points_arr_t &points, const spectrum_t &spectrum);

#endif // SPECTRUM_H
