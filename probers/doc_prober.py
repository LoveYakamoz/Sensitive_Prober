import docx

from probers.prober import Prober
from utils.log import logger


class Doc_Prober(Prober):
    """
    Docx & Doc文档检测
    """

    def __init__(self, file, sensitive_list):
        super(Doc_Prober, self).__init__(file, sensitive_list)

    def start_probe(self):
        print("=====> %s" % self._file)
        if "docx" in self._file:
            try:
                doc = docx.Document(self._file)
                for para in doc.paragraphs:
                    text = para.text.strip()
                    if text == "":
                        continue
                    for sensitive in self._sensitive_list:
                        if sensitive in text and sensitive not in self._result_list:
                            self._result_list.append(sensitive)
            except Exception as e:
                logger.error("file: %s error: %s", self._file, e)
            finally:
                pass
        else:
            # Todo process doc file
            pass

    def end_probe(self):
        if len(self._result_list) > 0:
            logger.info(self)
        else:
            pass
