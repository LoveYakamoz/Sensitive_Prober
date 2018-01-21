import xlrd

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
        try:
            datasheets = xlrd.open_workbook(self._file)
            for table in datasheets.sheets():
                nrows = table.nrows
                for i in range(nrows):
                    text = table.row_values(i)
                    for sensitive in self._sensitive_list:
                        if sensitive in text and sensitive not in self._result_list:
                            self._result_list.append(sensitive)
        except Exception as e:
            logger.error(str(e))

    def end_probe(self):
        if len(self._result_list) > 0:
            logger.info(self)
        else:
            pass
