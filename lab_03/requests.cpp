#include "requests.h"

err_t handle_request(const request_t &request)
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
    default:
        break;
    }

    return rc;
}
