# 適当にcutかけて飛跡を見るやつ
# ifガードをいじってcut条件を変えて使う
# Usage:
#     mkdir drawTracks
#     python3 drawTracks.py

import ROOT as r

ene_l_range = (50, 100)
length_range = (10, 100)

r.gROOT.SetBatch()

file = r.TFile.Open("cvvar.root")
tree = file.cvvar_tree

c = r.TCanvas('', '', 1000, 500)
c.Divide(2, 1)

pic_index = 0
for event in tree:
    if not ene_l_range[0] < event.ene_l < ene_l_range[1]:
        continue
    if not length_range[0] < event.length < length_range[1]:
        continue

    hist_xz = r.TH2D("hist_xz", f"hist_xz length={event.length};x_xz;z_xz",
                     100, -15, 15,
                     100, -15, 15)

    hist_yz = r.TH2D("hist_yz", f"hist_yz envNum={event.evtNum};y_yz;z_yz",
                     100, -15, 15,
                     100, -15, 15)

    for i in range(len(event.x_xz)):
        hist_xz.Fill(event.x_xz[i], event.z_xz[i])

    for i in range(len(event.y_yz)):
        hist_yz.Fill(event.y_yz[i], event.z_yz[i])

    c.cd(1)
    hist_xz.Draw('colz')
    c.cd(2)
    hist_yz.Draw('colz')

    c.SaveAs(f'drawTracks/{pic_index}.png')
    pic_index += 1

    del hist_xz
    del hist_yz
