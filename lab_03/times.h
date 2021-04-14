#ifndef TIMES_H
#define TIMES_H

#include "errors.h"
#include "dda.h"
#include "brezenham.h"
#include "wu.h"

#define ALGORITHM_NUM 6

err_t get_times(long long int times[ALGORITHM_NUM]);

#endif // TIMES_H
