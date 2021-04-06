#ifndef TIMES_H
#define TIMES_H

#include "errors.h"
#include "dda.h"
#include "brezenham.h"

#define ALGORITHM_NUM 5

err_t get_times(long long int times[ALGORITHM_NUM]);

#endif // TIMES_H
