#include "requests.h"

err_t handle_request(request_t &request)
{
    err_t rc = OK;

    switch (request.code)
    {
    case SEGMENT:
        rc = get_segment(request.segment_config);
        break;
    case SPECTRUM:
        rc = get_spectrum(request.spectrum_config);
        break;
    case TIME:
        rc = get_times(request.time_config);
        break;
    case CLEAR:
        clear_canvas(request.clear_config);
        break;
    default:
        break;
    }

    return rc;
}
