import ROOT as r
import uuid

CVVAR_ROOTFILE = "cvvar.root"


class CvvarReader:
    tree: r.TTree
    tfile: r.TFile
    canvas: r.TCanvas

    def __init__(self) -> None:
        self.open_cvvar()

    def open_cvvar(self) -> None:
        """
        カレントディレクトリのcvvar.rootを開く
        """
        self.tfile = r.TFile.Open(CVVAR_ROOTFILE)
        self.tree = self.tfile.cvvar_tree

    def save(self, object: r.TObject, opt: str, save_as: str, logz=False) -> str:
        """
        objectをcanvasにdrawして保存する\n
        ex) `reader.save(hist, 'hist.png')`
        """
        self.canvas = r.TCanvas()
        object.Draw(opt)
        if logz:
            r.gPad.SetLogz()

        self.canvas.SaveAs(save_as)

    def hist(self, branch: str, hist_arguments: str, draw_arguments: str = "", logz=False, logy=False) -> None:
        """
        あるブランチのヒストグラムを作成する\n

        ex) ene_lの0-1000を100binでdraw\n
        `reader.hist('ene_l', '100, 0, 1000')`\n

        ex) enel vs lentghの2d hist (0-50keV, 0-5cm) \n
        `reader.hist('length:ene_l', '100, 0, 50, 100, 0, 5', draw_arguments='colz')`\n
        """
        id = uuid.uuid1()

        c = r.TCanvas('canvas_{id}')
        if logy:
            r.gPad.SetLogy()
        if logz:
            r.gPad.SetLogz()

        hist_name = f'hist_{id}'
        self.tree.Draw(f'{branch}>>{hist_name}({hist_arguments})')
        hist = r.gROOT.FindObject(hist_name)

        hist.Draw(draw_arguments)
        c.SaveAs(f'{hist_name}.png')
