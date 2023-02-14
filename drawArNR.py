# ArのNRを探してみるマクロ
# Usage:
#     pwd -> /path/to/perXXXX
#     python3 drawArNR.py

import ROOT as r

from lib.file import CvvarReader
from lib.settings import set_batch

set_batch(True)

CUT_CONDITION = 'anode_nhit <= 3 && cathode_nhit <= 3 && ene_l < 50'

reader = CvvarReader()
livetime = reader.tree.__iter__().__next__().livetime
reader.tree.Draw('ene_l>>h(100, 0, 40)', CUT_CONDITION)
# reader.tree.Draw('length:ene_l>>h', CUT_CONDITION)
hist = r.gROOT.FindObject('h')
hist.Scale(reader.tree.GetEntries() / livetime)
reader.save(hist, '', 'arnr_energy.png')
