import ROOT as r
from lib.file import CvvarReader
from lib.settings import set_batch

ENERGY_RANGE = (0, 3000)
LENGTH_RANGE = (0, 50)

set_batch(True)
reader = CvvarReader()

hist = r.TH2D("hist", "energy vs length;energy;length",
              100, *ENERGY_RANGE,
              100, *LENGTH_RANGE)

for e in reader.tree:
    hist.Fill(e.ene_l, e.length)

reader.save(hist, "colz", "drawEnergyVsLength.png")
