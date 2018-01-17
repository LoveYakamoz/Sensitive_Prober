from probers.prober import Prober
from utils.log import logger


class Planttext_Prober(Prober):
    """
    文本（txt, bat, 源码文件等）文档检测
    """

    def __init__(self, file, sensitive_list):
        super(Planttext_Prober, self).__init__(file, sensitive_list)

    def start_probe(self):
        print("=====> %s" % self._file)
        try:
            f = open(self._file)
            for line in f.readlines():
                line = line.strip()
                if line == "":
                    continue
                else:
                    for sensitive in self._sensitive_list:
                        if sensitive in line and sensitive not in self._result_list:
                            self._result_list.append(sensitive)
        except Exception as e:
            logger.error("file: %s error: %s", self._file, e)
        finally:
            pass

    def end_probe(self):
        if len(self._result_list) > 0:
            logger.info(self)
        else:
            pass
