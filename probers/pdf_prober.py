from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf

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

        def read_pdf(pdf):
            rsrcmgr = PDFResourceManager()
            retstr = StringIO()
            laparams = LAParams()
            device = TextConverter(rsrcmgr, retstr, laparams=laparams)

            process_pdf(rsrcmgr, device, pdf)
            device.close()

            content = retstr.getvalue()
            retstr.close()
            return content

        content = read_pdf(self._file)

        for sensitive in self._sensitive_list:
            if sensitive in content and sensitive not in self._result_list:
                self._result_list.append(sensitive)

    def end_probe(self):
        if len(self._result_list) > 0:
            logger.info(self)
        else:
            pass
