import ROOT as r


def set_batch(is_batch: bool) -> None:
    """
    gROOT->SetBatch(bool)のエイリアス
    """
    r.gROOT.SetBatch(is_batch)
