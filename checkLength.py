import ROOT as r

r.gROOT.SetBatch()

file = r.TFile.Open("cvvar.root")
tree = file.cvvar_tree

c = r.TCanvas('', '', 1000, 500)
c.Divide(2, 1)

pic_index = 0
for event in tree:
    if not 1900 < event.length < 2100:
        continue

    hist_xz = r.TH2D("hist_xz", f"hist_xz length={event.length};x_xz;z_xz",
                     100, -15, 15,
                     100, -30, 30)

    hist_yz = r.TH2D("hist_yz", f"hist_yz envNum={event.evtNum};y_yz;z_yz",
                     100, -15, 15,
                     100, -30, 30)

    for i in range(len(event.x_xz)):
        hist_xz.Fill(event.x_xz[i], event.z_xz[i])

    for i in range(len(event.y_yz)):
        hist_yz.Fill(event.y_yz[i], event.z_yz[i])

    c.cd(1)
    hist_xz.Draw('colz')
    c.cd(2)
    hist_yz.Draw('colz')

    c.SaveAs(f'checkLength/{pic_index}.png')
    pic_index += 1
