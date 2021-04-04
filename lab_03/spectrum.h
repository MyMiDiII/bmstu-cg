#ifndef SPECTRUM_H
#define SPECTRUM_H

#include "draw.h"
#include "segments.h"
#include "errors.h"
#include "dda.h"

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

err_t get_spectrum(const spectrum_request_t &spectrum_config);

#endif // SPECTRUM_H
