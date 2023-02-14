# 6ボードの同期を示すplotを作成する
# ボードごとのデータを clock vs trigerIDの2Dhistにプロットする
# Usage:
#     python3 check_sync_6boards.py

import ROOT as r
# r.gROOT.SetBatch()
# r.gStyle.SetOptStat(1)

trigger_counter_range = (15, 400)
trigger_counter_bin = 3 * (trigger_counter_range[1] - trigger_counter_range[0])

clock_counter_range = (1.5e4, 40e4)
clock_counter_bin = 3 * (trigger_counter_range[1] - trigger_counter_range[0])

draw_arg = 'trigger_counter:clock_counter>>h({}, {}, {}, {}, {}, {})'.format(
    clock_counter_bin,
    *clock_counter_range,
    trigger_counter_bin,
    *trigger_counter_range
)

from typing import Dict
def check_6(fileID: int) -> Dict[int, int]:
    chain = r.TChain("tree01")
    chain.Add(f"GBKB-*_{fileID:04}.root")
    chain.Draw(draw_arg, "", "colz")

    h = r.gROOT.FindObject("h")
    counter = dict()
    for i in range(h.GetNbinsX()):
        for j in range(h.GetNbinsY()):
            bin_count = h.GetBinContent(i, j)
            counter[bin_count] = counter.get(bin_count, 0) + 1
    return counter


h = r.TH1D("", "", 8, 0-0.5, 8-0.5)
for file_id in range(0, 9):
    for board_count, event_count in check_6(file_id).items():
        if board_count == 0: continue
        for _ in range(event_count):
            h.Fill(board_count)

c = r.TCanvas()
h.Draw()
c.Draw()
# c.SaveAs("check_sync_6boards.png")
