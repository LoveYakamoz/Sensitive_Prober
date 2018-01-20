from probers.prober import Prober
from utils.log import logger


class Excel_Prober(Prober):
    """
    excel, csv, xls等文档检测
    """

    def __init__(self, file, sensitive_list):
        super(Excel_Prober, self).__init__(file, sensitive_list)

    def start_probe(self):
        print("=====> %s" % self._file)
        if self._file in ["xlsx", "csv", "xlsm", "xlm"]:
            pass
        else:
            pass

    def end_probe(self):
        if len(self._result_list) > 0:
            logger.info(self)
        else:
            pass
