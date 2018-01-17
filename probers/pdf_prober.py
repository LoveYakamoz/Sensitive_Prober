from probers.prober import Prober
from utils.log import logger


class Pdf_Prober(Prober):
    """
    pdf文档检测
    """

    def __init__(self, file, sensitive_list):
        super(Pdf_Prober, self).__init__(file, sensitive_list)

    def start_probe(self):
        print("=====> %s" % self._file)
        pass

    def end_probe(self):
        if len(self._result_list) > 0:
            logger.info(self)
        else:
            pass
