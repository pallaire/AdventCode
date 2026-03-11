#ifndef __PCHRONO__
#define __PCHRONO__

#include "ptypes.h"

u64 pchronoGetMicroSeconds();
void pchronoPrint(u64 ts, const char* label);

#endif
