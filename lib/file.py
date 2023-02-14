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

    def save(self, object: r.TObject, opt: str, save_as: str) -> str:
        """
        objectをcanvasにdrawして保存する\n
        ex) `reader.save(hist, 'hist.png')`
        """
        self.canvas = r.TCanvas()
        object.Draw(opt)
        self.canvas.SaveAs(save_as)

    def hist(self, branch: str) -> None:
        """
        あるブランチのヒストグラムを作成する\n
        ex) `reader.hist('ene_l')`
        """
        id = uuid.uuid1()
        hist_name = f'hist_{id}'
        self.tree.Draw(f'{branch}>>{hist_name}')
        hist = r.gROOT.FindObject(hist_name)

        c = r.TCanvas('canvas_{id}')
        hist.Draw()
        c.SaveAs(f'{hist_name}.png')
