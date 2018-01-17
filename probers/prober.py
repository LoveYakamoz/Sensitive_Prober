import abc


class Prober(metaclass=abc.ABCMeta):
    """

    """

    def __init__(self, file, sensitive_list):
        self._file = file
        self._sensitive_list = sensitive_list
        self._result_list = []

    def __repr__(self):
        return "file: {}, contains sensitive words: {}".format(self._file, self._result_list)

    @abc.abstractmethod
    def start_probe(self):
        pass

    @abc.abstractmethod
    def end_probe(self):
        pass

    def process(self):
        self.start_probe()
        self.end_probe()
