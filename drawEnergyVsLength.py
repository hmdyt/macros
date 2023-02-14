import ROOT as r

ENERGY_RANGE = (0, 3000)
LENGTH_RANGE = (0, 50)

r.gROOT.SetBatch()

file = r.TFile.Open("cvvar.root")
tree = file.cvvar_tree

c = r.TCanvas()

hist = r.TH2D("hist", "energy vs length;energy;length",
              100, *ENERGY_RANGE,
              100, *LENGTH_RANGE)

for e in tree:
    hist.Fill(e.ene_l, e.length)

hist.Draw("colz")
c.SaveAs("drawEnergyVsLength.png")
