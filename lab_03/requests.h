#ifndef REQUESTS_H
#define REQUESTS_H

#include "segments.h"
#include "spectrum.h"
#include "draw.h"
#include "errors.h"
#include "times.h"

enum request_code_t
{
    SEGMENT,
    SPECTRUM,
    TIME,
    CLEAR
};

struct request_t
{
    request_code_t code;
    union
    {
        segment_request_t segment_config;
        spectrum_request_t spectrum_config;
        long long int *time_config;
        canvas_t clear_config;
    };
};

err_t handle_request(const request_t &request);

#endif // REQUESTS_H
