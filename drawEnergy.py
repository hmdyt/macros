from lib.file import CvvarReader
from lib.settings import set_batch

set_batch(True)

reader = CvvarReader()
reader.hist('ene_l')
