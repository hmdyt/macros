# エネルギーvs飛跡長をplotする
# Usage:
#     pwd -> /path/to/perXXXX
#     python3 drawEnergyVsLength.py

import ROOT as r
from lib.file import CvvarReader
from lib.settings import set_batch

ENERGY_RANGE = (0, 100)
LENGTH_RANGE = (0, 0.02)

set_batch(True)
reader = CvvarReader()
reader.hist(
    "length:ene_l",
    f"100, {ENERGY_RANGE[0]}, {ENERGY_RANGE[1]}, 100, {LENGTH_RANGE[0]}, {LENGTH_RANGE[1]}",
    draw_arguments="colz",
    logz=True
)
